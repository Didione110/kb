import { defineConfig } from "vitepress";
import sidebar from "./sidebar.gen.json" with { type: "json" };

export default defineConfig({
  lang: "zh-CN",
  title: "科情客服知识库",
  description: "基于钉钉知识库与 AI 表格构建的客服智能知识库",
  lastUpdated: true,
  cleanUrls: true,
  srcDir: "docs",
  ignoreDeadLinks: true,

  head: [
    ["meta", { name: "theme-color", content: "#0ea5e9" }],
  ],

  themeConfig: {
    logo: "/logo.svg",
    nav: [
      { text: "首页", link: "/" },
      { text: "知识库", link: "/kb/" },
      { text: "使用指南", link: "/guide/" },
      { text: "API", link: "/api/" },
      { text: "维护", link: "/maintain/" },
    ],
    sidebar: {
      "/kb/": [
        { text: "知识库总览", link: "/kb/" },
        ...sidebar,
      ],
      "/guide/": [
        {
          text: "使用指南",
          items: [
            { text: "快速开始", link: "/guide/" },
            { text: "搜索知识", link: "/guide/search" },
            { text: "引用与溯源", link: "/guide/citation" },
          ],
        },
      ],
      "/maintain/": [
        {
          text: "知识维护",
          items: [
            { text: "维护流程", link: "/maintain/" },
            { text: "新增知识", link: "/maintain/add" },
            { text: "数据同步", link: "/maintain/sync" },
            { text: "部署发布", link: "/maintain/deploy" },
          ],
        },
      ],
    },
    search: {
      provider: "local",
      options: {
        translations: {
          button: { buttonText: "搜索知识库", buttonAriaLabel: "搜索知识库" },
          modal: {
            noResultsText: "未找到相关结果",
            resetButtonTitle: "清除查询",
            footer: { selectText: "选择", navigateText: "切换", closeText: "关闭" },
          },
        },
      },
    },
    outline: { label: "本页目录", level: [2, 3] },
    docFooter: { prev: "上一篇", next: "下一篇" },
    darkModeSwitchLabel: "外观",
    sidebarMenuLabel: "菜单",
    returnToTopLabel: "回到顶部",
    lastUpdated: { text: "最后更新于" },
    footer: {
      message: "科情客服知识库 · 单一事实源：钉钉知识库 + AI 表格",
      copyright: "仅供内部使用",
    },
  },
});
