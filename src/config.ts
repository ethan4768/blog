import type { Site, SocialObjects } from "./types";

export const SITE: Site = {
  website: "https://blog.finengine.tech/",
  profile: "https://blog.finengine.tech/",
  author: "ethan4768",
  desc: "寻岳的网络日志",
  title: "寻岳的网络日志",
  ogImage: "https://images.finengine.tech/favicon.ico",
  lightAndDarkMode: true,
  articleCountPerIndex: 4,
  articleCountPerPage: 8,
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
  showArchives: false,
};

export const LOCALE = {
  lang: "en", // html lang code. Set this empty and default will be "en"
  langTag: ["en-EN",  "zh-CN"], // BCP 47 Language Tags. Set this empty [] to use the environment default
} as const;

export const LOGO_IMAGE = {
  enable: false,
  svg: true,
  width: 216,
  height: 46,
};

export const SOCIALS: SocialObjects = [
  {
    name: "Github",
    href: "https://github.com/ethan4768",
    linkTitle: `ethan4768 on Github`,
    active: true,
  },
  {
    name: "Twitter",
    href: "https://twitter.com/ethan4768",
    linkTitle: `ethan4768 on Twitter`,
    active: true,
  },
  {
    name: "Mail",
    href: "mailto:finengine.tech@gmail.com",
    linkTitle: `Send an email to finengine.tech@gmail.com`,
    active: true,
  },
];