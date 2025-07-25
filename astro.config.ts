import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import react from "@astrojs/react";
import sitemap from "@astrojs/sitemap";
import mdx from "@astrojs/mdx";
import { SITE } from "./src/config";

// https://astro.build/config
export default defineConfig({
  site: SITE.website,
  integrations: [tailwind({
    applyBaseStyles: false,
  }), react(), sitemap(), mdx()],
  markdown: {
    shikiConfig: {
      // For more themes, visit https://shiki.style/themes
      themes: { light: "min-light", dark: "night-owl" },
      wrap: true,
    },
  },
  vite: {
    optimizeDeps: {
      exclude: ["@resvg/resvg-js"],
    },
    build: {
      rollupOptions: {
        onwarn(warning, warn) {
          if (warning.code === 'UNRESOLVED_IMPORT') {
            console.warn(`⚠️  Skipping unresolved import: ${warning.source}`);
            return;
          }
          warn(warning);
        },
      },
    },
  },
  scopedStyleStrategy: "where",
  experimental: {
    contentLayer: true,
  },
});