import { SITE } from "@config";
import { glob } from "astro/loaders";
import { defineCollection, type SchemaContext, z } from "astro:content";

const defaultSchema = ({ image }: SchemaContext) =>
  z.object({
    author: z.string().default(SITE.author),
    pubDatetime: z.date(),
    modDatetime: z.date().optional().nullable(),
    title: z.string(),
    featured: z.boolean().optional(),
    draft: z.boolean().optional(),
    tags: z.array(z.string()).default(["others"]),
    ogImage: image()
      .refine(img => img.width >= 1200 && img.height >= 630, {
        message: "OpenGraph image must be at least 1200 X 630 pixels!",
      })
      .or(z.string())
      .nullable()
      .optional(),
    description: z.string(),
    canonicalURL: z.string().optional(),
    slug: z.string().optional(),
    monthlyCollection: z.boolean().optional(),
  });

const posts = defineCollection({
  type: "content_layer",
  loader: glob({ pattern: "**/*.md", base: "./src/content/posts" }),
  schema: defaultSchema,
});

const bookmarks = defineCollection({
  type: "content_layer",
  loader: glob({ pattern: "**/*.md", base: "./src/content/bookmarks" }),
  schema: defaultSchema,
});

const favorites = defineCollection({
  type: "content_layer",
  loader: glob({ pattern: "**/*.md", base: "./src/content/favorites" }),
  schema: defaultSchema,
});

// noinspection JSUnusedGlobalSymbols
export const collections = { posts, bookmarks, favorites };
