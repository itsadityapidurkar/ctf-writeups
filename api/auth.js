export default function handler(req, res) {
  const client_id = process.env.OAUTH_CLIENT_ID;
  if (!client_id) {
    return res.status(500).send("OAUTH_CLIENT_ID environment variable is missing.");
  }
  const scope = "repo";
  const state = Math.random().toString(36).substring(2, 15);
  
  res.redirect(`https://github.com/login/oauth/authorize?client_id=${client_id}&scope=${scope}&state=${state}`);
}
