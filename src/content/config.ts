import { defineCollection, z } from 'astro:content';

const writeups = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string().optional(),
    ctfId: z.string().optional(),
    category: z.string().optional(),
    difficulty: z.string().optional(),
    flag: z.string().optional(),
    banner: z.string().optional(),
    status: z.string().optional()
  }).optional(),
});

export const collections = {
  writeups,
};
