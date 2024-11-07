import type { CollectionEntry } from "astro:content";
import filter from "./filter.ts";

const getSortedArticles = (posts: CollectionEntry<"posts" | "favorites" | "bookmarks">[]) => {
  return posts
    .filter(filter)
    .sort(
      (a, b) =>
        Math.floor(
          new Date(b.data.modDatetime ?? b.data.pubDatetime).getTime() / 1000,
        ) -
        Math.floor(
          new Date(a.data.modDatetime ?? a.data.pubDatetime).getTime() / 1000,
        ),
    );
};

export default getSortedArticles;
