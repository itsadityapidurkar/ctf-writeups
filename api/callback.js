export default async function handler(req, res) {
  const { code } = req.query;
  const client_id = process.env.OAUTH_CLIENT_ID;
  const client_secret = process.env.OAUTH_CLIENT_SECRET;

  if (!code) {
    return res.status(400).send("No code provided from GitHub callback.");
  }
  if (!client_id || !client_secret) {
    return res.status(500).send("OAUTH_CLIENT_ID or OAUTH_CLIENT_SECRET environment variable is missing.");
  }

  try {
    const response = await fetch("https://github.com/login/oauth/access_token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        client_id,
        client_secret,
        code,
      }),
    });

    const data = await response.json();

    if (data.error) {
      return res.status(400).send(`GitHub OAuth Error: ${data.error_description || data.error}`);
    }

    const token = data.access_token;
    res.setHeader("Content-Type", "text/html");
    return res.send(`
      <!DOCTYPE html>
      <html>
      <head>
        <title>Authorized</title>
      </head>
      <body>
        <script>
          const target = window.opener || window.parent;
          if (target) {
            // 1. Signal to Decap CMS that authorization has started (required handshake)
            target.postMessage("authorizing:github", "*");
            
            // 2. Send the successful access token
            target.postMessage(
              'authorization:github:success:${JSON.stringify({ token, provider: "github" })}',
              '*'
            );
            
            setTimeout(() => {
              window.close();
            }, 100);
          }
        </script>
        <p>Authorized successfully. You can close this window now.</p>
      </body>
      </html>
    `);
  } catch (error) {
    console.error("Error during GitHub OAuth callback exchange:", error);
    return res.status(500).send("An error occurred during token exchange callback.");
  }
}
