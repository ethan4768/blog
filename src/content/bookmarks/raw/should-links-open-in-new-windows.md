---
title: 链接是否应该在新窗口中打开？ - Smashing Magazine
description: 在Smashing Magazine的文章中，探讨了链接是否应该在新窗口中打开的问题。尽管这个决定在初看时似乎与网站的性质及访客的偏好有关，但综上所述，答案是：不，链接不应该在新窗口中打开。
pubDatetime: 2024-11-07T18:09:54+08:00
ogImage: https://archive.smashing.media/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/d58a3abd-e671-45af-9e34-4baf896b3b1a/openlink.jpg
tags: 
  - raw
---

[原文链接](https://www.smashingmagazine.com/2008/07/should-links-open-in-new-windows/) | [原文内容](../raw/should-links-open-in-new-windows) | [AI 总结](../summary/should-links-open-in-new-windows)

---

*   11 min read
*   [UX](https://www.smashingmagazine.com/category/ux), [JavaScript](https://www.smashingmagazine.com/category/javascript), [Tabs](https://www.smashingmagazine.com/category/tabs), [Usability](https://www.smashingmagazine.com/category/usability), [UX](https://www.smashingmagazine.com/category/ux)

**No, they shouldn’t**. At first glance the decision to open links in new windows or not depends on the given site and the preferences of its visitors.

Visitors to the sites with heavy linking are more willing to have links opened in new windows then open dozens of links in new windows manually.

Visitors of less-heavy-linkage-sites are more likely to open some particular link in new window to remain on the site and continue to browse through it afterward. However, this is not true.

Users also don’t like to deal with dozens of opened tabs and some visitors tend to become quickly angry with the disabled back button. Furthermore, some visitors may not even realize that a new window was opened and hit the back-button mercilessly — without any result. That’s not user-friendly, and that’s not a good user experience we, web designers, strive for.

### Place users in control

From the usability point of view the decision to enforce opening links in new windows violates one of the fundamental principles of the user interface design: users should always **be in control** of the interface they are interacting with.

Leading user interface and usability researchers such as

*   [Ben Shneiderman](https://faculty.washington.edu/jtenenbg/courses/360/f04/sessions/schneidermanGoldenRules.html) (_8 Golden Rules of Interface Design_),
*   [Theo Mandel](https://www.theomandel.com/docs/Mandel-GoldenRules.pdf) (_User Interface Design Principles_)
*   [Bruce Tognazzini](https://www.asktog.com/basics/firstPrinciples.html) (_First Principles of Interaction Design_)

claim that a user-friendly and **effective user interface places users in control of the application** they are using.

Users need to be able to rely on consistency of the user interface and know that they won’t be distracted or disrupted during the interaction. Users must know, understand and anticipate what is going on and what will happen once user interface elements are used. Any deviations from this convention result in a more design-oriented and less user-oriented design.

As [Shneiderman claims](https://www.smashingmagazine.com/2007/10/09/30-usability-issues-to-be-aware-of/), experienced users strongly desire the sense that they are in charge of the system and that the system responds to their actions. As designers, it is our duty to design the system to make users the initiators of actions rather than the responders.

Designers are tempted to enforce users to actually use the interface or browse through the site they have created. Although the rationale behind stems from some clear commercial objectives and therefore often preferred by project managers, it is the designer’s duty to make clear to managers that **users do not care**.

In fact, developers often tend to forget a simple, almost elementary fact: if users want to close the application or leave a site, they will — doesn’t matter which obstacles are placed on their path to the exit-button. The more obstacles there are the more negative the user experience will be.

As designers, it is our decision to provide users with a clear, unambiguous choice, but we have no right to decide for users which choice they make.

### Why enforcing opening links in new windows is wrong

Since users need to be placed in control of the interface they are interacting with, it is wrong to make decisions for them as designer’s decisions don’t necessarily match users’ decisions. The main problem with enforcing links to open in new windows is that this decision overrules user’s decision to control the view in their browser.

Since large websites (Google, Amazon, AOL, Yahoo & Co.) open links in the same window (unless it is explicitly stated that links are opened in new windows), users tend to assume that the link on an unknown page will be opened in the same window. So **users expect the link to be opened in the same window**.

Let us now consider the following two situations where a user doesn’t know upfront if the site opens links in new windows or the same window:

1.  user wants to open link in a new window, but the site opens links in the same window,
2.  user wants to open link in the same window, but the site opens links in new windows.

In the first situation users can choose to open a link in the new window using context-menu or shortcuts described in the next sections of this article. In this situation, users are the initiators of actions as they decide how the linked page should be displayed. Here site’s behavior meets user’s expectations resulting in a **good user experience**.

In the second situation users would simply click on the link and suddenly find out that the link is opened in a new window. In this situation users are the responders of actions as they need to react in the way how the linked page is displayed — for instance close the windows that was opened automatically. Furthermore, here site’s behavior doesn’t meet user’s expectations resulting in a **bad user experience**.

Users find it annoying when the site does something without asking them to do so. If users want to open new windows let them do so and don’t indulge their intelligence by making the decision for them otherwise. Don’t force a new window upon users unless there’s a excellent reason to do so.

### Every rule has an exception

Of course, there are exceptions: in some situations it is right to open links in new windows and wrong to open links in the same windows. Jakob Nielsen suggests to use new windows in case the linked document is not a .html-document. In this case, he recommends using a pop-up windows without browser control toolbar. In such case it is reasonable to let the user know upfront how the links will be opened.

A small warning icon usually suffices. However, you need to make sure that the link is unlikely to be misunderstood. After all, it is a common practice to use icons to inform the visitors that links lead to external websites. An additional or similar icon may produce irritation. Small usability tests may be helpful and necessary in this situation.

[![Image 1: Heise](https://archive.smashing.media/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/40a15fa3-fb25-431c-92ee-cb962e2f4543/heise.gif)](https://www.heise.de/tp/r4/artikel/28/28190/1.html)

[Telepolis](https://www.heise.de/tp/r4/artikel/28/28190/1.html) lets its visitors know that a link leads to the external page. However, the icon used may be misunderstood as it can also symbolize opening links in new windows.

It is appropriate to enforce opening links in a new window in case

*   **the link provides assistance** or help. If you are on a shopping cart page, and users click on a “help” link. In that case, users don’t want to navigate away from the cart page, so a new window is acceptable. In such cases dynamic tooltips are usually better than pop-ups that are again better than opening new windows.
*   **the link may interrupt an ongoing process**. For instance, if users are filling a web-form and the form provides the link to terms of service or privacy policy below the form it is reasonable to enforce this link to open in a new window to not interrupt the ongoing process. This is important in sign-up forms and crucial in checkout-forms. Otherwise, users may lose the information they’ve already typed in and close the browser window in response.
*   **the link leads to a non-html-document**. E.g. .pdf-file, .xls-file, .mp3 and so on. Warn users in advance that a new window will appear. When using PC-native file formats such as PDF or spreadsheets, users feel like they’re interacting with a PC application. Because users are no longer browsing a website, they shouldn’t be given a browser UI. Best of all, prevent the browser from opening the document in the first place.
*   **the link leads to a large image which takes time to load**. Opening this image in a new window allows user to focus on your content while the image is being loaded in the background.

### Forgive them, for they don’t know what they do

Unfortunately, we weren’t able to find any recent research findings that would provide us with a better understanding of how users open links if they want to open them in new tabs or windows. However, it is likely to assume that most **users don’t know shortcuts** and prefer more intuitive straight solutions. More experienced users are more likely to use shortcuts that are described below as well.

There are three reasonable ways for opening links in new windows. Most users use the first option — not because it is the most efficient one, but because it is the most obvious one. These options are implemented in all modern browsers; older browsers may have problems with the second and third options, though.

1.  visitors use the **context-menu**: users click with the right mouse on the link and select the option “Open link in a new tab/window”. If the link is opened in a new tab, the active window remains the same as it was before the click. If the link is opened in a new window, new window appears, and the new window becomes the active window.
2.  visitors use the **Ctrl+click-shortcut**: users press the Ctrl+key and click with the left mouse button on the link. The link is automatically opened in a new tab. The active window remains the same as it was before the click. This shortcut can vary depending on the operating system and the browser implementation.
3.  visitors use the **middle-click**: users point the mouse pointer to the link and press the middle-click of the mouse. The link is automatically opened in a new tab. The active window remains the same as it was before the click.

The first option is definitely the most ineffective yet most popular one. It requires more clicks and more concentration, therefore more time and more cognitive load on the user. The third one is the quickest one as users don’t need to permanently switch between the context-menu and the page itself.

[![Image 2: Open links in new tabs](https://archive.smashing.media/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/4d8e5f7c-bbe5-43c0-b6d9-ff73cfd05e8a/tab.gif)](https://www.smashingmagazine.com/images/opening-links/tab.gif)

Most users seem to use the context-menu to open links in new tabs or windows. [Image source](https://www.scrollinondubs.com/2006/10/).

The main irritation from the users’ side comes from the fact that most users know only the first option. Consequently, if they want to open links in new windows they _need_ to use the context-menu, with multiple clicks, switching the view back and forth again and again. That’s stressful and unpleasant. Still, opening links in the same window (by default) is the **lesser of two evils**. And if users don’t know how to do it quickly, tell them explicitly — they will be grateful for your help.

### But I can force visitors to stay on my site, right?

_No._ Even if you enforce the external links to open in new windows users will find their way around to open the link on the same page if they want to:

1.  users can **copy the link**, paste it in the address bar and hit the return button; the link will be opened in the same window.
2.  users can **drag the link** to the address bar; the link will be opened in the same window.

Unfortunately, not every single browser allows users to do that. However, modern browsers have this functionality implemented since years. If users don’t want a link to open in a new window, they’ll try to find the way to circumvent designer’s decision.

[![Image 3: Firefox](https://archive.smashing.media/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/086d7379-24a4-4c16-bdcc-ba2c51d470ae/firefox.jpg)](https://www.smashingmagazine.com/images/opening-links/firefox.jpg)

Firefox enables its users to decide how the links designer has chosen to open in new windows should be opened.

Therefore, from the designer’s perspective, it is better to provide users with a clear and clean way to do so respecting their interests and not neglecting their time. If you want your visitors to come back, assist them, guide them, help them, but never impose on their patience and willingness to browse on your site.

### Optimal solution

In our opinion the most effective and user-friendly solution is to allow users to select how the links should be opened. However, they don’t have to do that via their browser. Designers can provide users with a small check-box that “decides” how the links should be opened. You need to make sure that the checkbox is visible and users understand what it is good for.

This can be done via JavaScript. Once the box is checked all links will be opened in a new tab / window. Just check the box yourself and try it out:

Source code for the check-box:

```
<form>
<input type="checkbox" onclick="linkopener(this.checked)" id="linksnewwin">
Open external links in a new tab?
</form>
```

Source code for the JavaScript (you’ll need to replace _domain.com_ with your web-site’s URL; thus the browser will be able to distinguish between internal and external links):

```
<script language="javascript">

function linkopener(a) {
var b = a ? "_blank" : "_self";
var c = document.links;

for (var i=0; i < c.length; i++) {
  if (c[i].href.search("domain.com") == -1) c[i].target = b;
}

}

</script>
```

This JavaScript doesn’t use cookies so if users browse from one side to another their preference won’t be stored. If you’d like the checkbox to work throughout your site you’ll have to consider using cookies to store users’ preferences.

### Bottom line

It is important that users are placed in control of the user interface they are using. Since users expect the link to be opened in the same window, set your links to open in the same window. Don’t force a new window upon users unless there’s a very good reason to do so. For the latter purpose, consider opening links in new windows if the link provides assistance or help, if it may interrupt an ongoing process or it leads to a non-html-document.

Allow users to select how the links should be opened on a given web-site. Opening links in the same windows the lesser of two evils. And if users don’t know how to do it quickly, tell them explicitly — they will be grateful for your help.

### Sources and Resources

*   [Beware of Opening Links in a New Window](https://www.sitepoint.com/article/beware-opening-links-new-window) (Sitepoint)
*   [Should Links Open in a New Window?](https://www.problogger.net/archives/2007/06/26/should-links-open-in-a-new-window/) (Problogger)
*   [New Window for a New Link?](https://www.problogdesign.com/blog-usability/new-window-for-a-new-link/) (Pro Blog Design)
*   [Avoid forcing to open in a new window](https://www.webnauts.net/new-window.html) (Webnauts)
*   [Debate: Should New Links Open in New Tabs/Windows?](https://gracefulflavor.net/2008/01/14/debate-should-new-links-open-in-new-tabswindows/) (GracefulFlavor)
*   [Should links open in a new window?](https://www.davidairey.com/should-links-open-in-a-new-window/ "Should links open in a new window?") (David Airey)
*   [DontOpenNewWindow](https://css-discuss.incutio.com/?action=find&find=DontOpenNewWindow) (CSS-Discuss)
*   [Open External Links in New Window Automatically](https://cssglobe.com/post/1281/open-external-links-in-new-window-automatically)
*   [Using JavaScript instead of target to open new windows](https://www.456bereastreet.com/archive/200610/opening_new_windows_with_javascript_version_12/)
