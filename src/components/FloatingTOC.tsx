import tocbot from "tocbot";
import { useEffect } from "react";

export default function FloatingTOC(props: { collapseDepth?: number }) {
  useEffect(() => {
    tocbot.init({
      // Where to render the table of contents.
      tocSelector: "#floating-toc",
      // Where to grab the headings to build the table of contents.
      contentSelector: "#article",
      // Which headings to grab inside the contentSelector element.
      headingSelector: "h1, h2, h3, h4, h5, h6",
      // For headings inside relative or absolute positioned containers within content.
      hasInnerContainers: true,
      collapseDepth: props.collapseDepth ?? 3,
    });
    return tocbot.destroy;
  }, []);
  return null;
}
