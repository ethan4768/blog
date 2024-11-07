import type { APIRoute } from "astro";
import { getCollection, type CollectionEntry } from "astro:content";
import { generateOgImageForPost } from "@utils/generateOgImages";
import { slugifyStr } from "@utils/slugify";

export async function getStaticPaths() {
  const favorites = await getCollection("favorites").then(p =>
    p.filter(({ data }) => !data.draft && !data.ogImage)
  );

  return favorites.map(post => ({
    params: { slug: slugifyStr(post.data.title) },
    props: post,
  }));
}

export const GET: APIRoute = async ({ props }) =>
  new Response(await generateOgImageForPost(props as CollectionEntry<"favorites">), {
    headers: { "Content-Type": "image/png" },
  });
