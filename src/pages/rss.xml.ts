import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import getSortedArticles from "@utils/sort.ts";
import { SITE } from "@config";

export async function GET() {
  const posts = await getCollection("posts");
  const bookmarks = await getCollection("bookmarks", ({ data }) => !data.monthlyCollection);
  const favorites = await getCollection("favorites");
  const allArticles = [...posts, ...bookmarks, ...favorites];

  const sortedArticles = getSortedArticles(allArticles);

  return rss({
    title: SITE.title,
    description: SITE.desc,
    site: SITE.website,
    items: sortedArticles.map(({ data, collection, slug }) => ({
      link: `${collection}/${slug}/`,
      title: data.title,
      description: data.description,
      pubDate: new Date(data.modDatetime ?? data.pubDatetime),
    })),
  });
}
