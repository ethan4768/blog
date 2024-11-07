import type { CollectionEntry } from "astro:content";
import getSortedArticles from "./sort.ts";
import { slugifyAll, slugifyStr } from "./slugify";
import filter from "@utils/filter.ts";

interface Tag {
  tag: string;
  tagName: string;
}

export const getArticlesByTag = (articles: CollectionEntry<"posts" | "favorites" | "bookmarks">[], tag: string) =>
  getSortedArticles(
    articles.filter(article => slugifyAll(article.data.tags).includes(tag)),
  );

export const getUniqueTags = (articles: CollectionEntry<"posts" | "favorites" | "bookmarks">[]) => {
  const tags: Tag[] = articles
    .filter(filter)
    .flatMap(post => post.data.tags)
    .map(tag => ({ tag: slugifyStr(tag), tagName: tag }))
    .filter(
      (value, index, self) =>
        self.findIndex(tag => tag.tag === value.tag) === index,
    )
    .sort((tagA, tagB) => tagA.tag.localeCompare(tagB.tag));
  return tags;
};