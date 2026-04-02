---
layout: default
title: 研究方向
---

{% include page-header.html header=site.research_header accent="cyan" %}

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-14 md:py-18">
  <div class="grid gap-10 xl:grid-cols-[0.62fr_1.38fr] xl:items-start">
    {% include chapter-intro.html
      serial="ATLAS"
      accent="sky"
      reveal="left"
      kicker_zh="快速索引"
      kicker_en="Quick Index"
      title_zh="先看目录，再决定从哪条研究链路进入"
      title_en="Start with the Atlas, Then Enter the Theme You Need"
      description_zh="这页不再只是顺序罗列方向，而是先给你一张可跳转的研究地图。你可以快速扫过主题，再进入具体章节查看图像、摘要与重点列表。"
      description_en="This page is no longer a simple vertical list. It starts as a navigable atlas so you can scan the themes first, then dive into images, summaries, and focus lists."
    %}

    <div class="exhibit-index" data-reveal="scale">
      {% for area in site.data.research %}
      <a href="#area-{{ forloop.index }}" class="exhibit-index__item">
        <span class="exhibit-index__num">0{{ forloop.index }}</span>
        <div class="min-w-0">
          <div class="flex items-center gap-3">
            <span class="text-2xl">{{ area.icon }}</span>
            <p class="text-lg font-black leading-tight text-slate-900 dark:text-white">
              <span class="lang-zh">{{ area.title.zh | default: area.title }}</span>
              <span class="lang-en">{{ area.title.en | default: area.title }}</span>
            </p>
          </div>
          <p class="mt-3 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
            <span class="lang-zh">{{ area.description.zh | default: area.description }}</span>
            <span class="lang-en">{{ area.description.en | default: area.description }}</span>
          </p>
        </div>
      </a>
      {% endfor %}
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pb-6">
  <div class="space-y-8 md:space-y-10">
    {% for area in site.data.research %}
    {% assign points_zh = area.points.zh | default: area.points %}
    {% assign points_en = area.points.en | default: area.points %}
    {% assign point_count = points_zh | size %}
    {% assign is_reverse = forloop.index0 | modulo: 2 %}

    <article id="area-{{ forloop.index }}" class="stage-shell research-stage px-6 py-8 md:px-10 md:py-10" data-stage="research" data-reveal="scale">
      <div class="research-stage__ghost">0{{ forloop.index }}</div>

      <div class="grid gap-8 xl:grid-cols-[1.05fr_0.95fr] xl:items-start">
        <div class="{% if is_reverse == 1 %}xl:order-2{% endif %}">
          <div class="flex flex-wrap items-center gap-3">
            <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-sky-50 text-4xl text-sky-600 dark:bg-slate-800 dark:text-cyan-300">{{ area.icon }}</div>
            <span class="chip text-[11px] font-black uppercase tracking-[0.16em] text-slate-500 dark:text-slate-300">
              <span class="lang-zh">章节 0{{ forloop.index }}</span>
              <span class="lang-en">Chapter 0{{ forloop.index }}</span>
            </span>
            <span class="chip text-[11px] font-black uppercase tracking-[0.16em] text-slate-500 dark:text-slate-300">
              {% if point_count > 0 %}
              <span class="lang-zh">{{ point_count }} 个重点</span>
              <span class="lang-en">{{ point_count }} focus points</span>
              {% else %}
              <span class="lang-zh">开放主题</span>
              <span class="lang-en">Open frontier</span>
              {% endif %}
            </span>
          </div>

          <h2 class="mt-7 text-3xl font-black leading-tight text-slate-900 dark:text-white md:text-4xl">
            <span class="lang-zh">{{ area.title.zh | default: area.title }}</span>
            <span class="lang-en">{{ area.title.en | default: area.title }}</span>
          </h2>

          <p class="mt-5 text-base leading-relaxed text-slate-600 dark:text-slate-300 md:text-lg">
            <span class="lang-zh">{{ area.description.zh | default: area.description }}</span>
            <span class="lang-en">{{ area.description.en | default: area.description }}</span>
          </p>

          {% unless area.image %}
          <div class="stage-rail mt-7 p-5">
            <p class="section-kicker text-[0.64rem] font-black uppercase text-sky-600 dark:text-cyan-300">
              <span class="lang-zh">展陈说明</span>
              <span class="lang-en">Curatorial Note</span>
            </p>
            <p class="mt-3 text-base font-bold leading-relaxed text-slate-900 dark:text-white">
              {% if point_count > 0 %}
              <span class="lang-zh">这一主题当前以知识结构和关键问题为主，不强制绑定单一图像，用文字关系来强调研究边界与方向。</span>
              <span class="lang-en">This theme is currently best expressed through its structure of ideas and key questions, so the section emphasizes textual relationships instead of a single representative image.</span>
              {% else %}
              <span class="lang-zh">这是一个正在持续展开的开放前沿，我们把它保留为轻量章节，用来展示实验室对未来问题的预判与布局。</span>
              <span class="lang-en">This is an actively expanding frontier. It is kept as a lighter section to show how the lab frames future questions and emerging opportunities.</span>
              {% endif %}
            </p>
          </div>
          {% endunless %}
        </div>

        <div class="{% if is_reverse == 1 %}xl:order-1{% endif %} space-y-5">
          {% if area.image %}
          <div class="research-media">
            <img src="{{ site.baseurl }}{{ area.image }}" alt="{{ area.title.zh | default: area.title }}" class="h-72 w-full object-cover md:h-80">
          </div>
          {% endif %}

          {% if point_count > 0 %}
          <div class="panel-surface p-6 md:p-7">
            <p class="section-kicker text-[0.68rem] font-black uppercase text-sky-600 dark:text-cyan-300">
              <span class="lang-zh">核心关注领域</span>
              <span class="lang-en">Key Focus Areas</span>
            </p>

            <ul class="mt-5 space-y-4 lang-zh">
              {% for point in points_zh %}
              <li class="flex items-start gap-3 text-sm font-semibold leading-relaxed text-slate-700 dark:text-slate-200 md:text-base">
                <span class="mt-1 inline-flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-sky-50 text-xs font-black text-sky-600 dark:bg-slate-800 dark:text-cyan-300">0{{ forloop.index }}</span>
                <span>{{ point }}</span>
              </li>
              {% endfor %}
            </ul>

            <ul class="mt-5 space-y-4 lang-en">
              {% for point in points_en %}
              <li class="flex items-start gap-3 text-sm font-semibold leading-relaxed text-slate-700 dark:text-slate-200 md:text-base">
                <span class="mt-1 inline-flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-sky-50 text-xs font-black text-sky-600 dark:bg-slate-800 dark:text-cyan-300">0{{ forloop.index }}</span>
                <span>{{ point }}</span>
              </li>
              {% endfor %}
            </ul>
          </div>
          {% else %}
          <div class="panel-surface p-6 md:p-7">
            <p class="section-kicker text-[0.68rem] font-black uppercase text-sky-600 dark:text-cyan-300">
              <span class="lang-zh">当前状态</span>
              <span class="lang-en">Current Status</span>
            </p>
            <p class="mt-4 text-base leading-relaxed text-slate-600 dark:text-slate-300">
              <span class="lang-zh">这一方向目前更像一个跨项目的战略主题，用来组织开放世界、长尾识别与知识迁移相关的问题。它不会被限制在单一数据集或单一实验范式里。</span>
              <span class="lang-en">This direction currently functions as a strategic cross-project theme, organizing questions around open-world recognition, long-tail understanding, and knowledge transfer rather than being constrained to a single dataset or experiment style.</span>
            </p>
          </div>
          {% endif %}
        </div>
      </div>
    </article>
    {% endfor %}
  </div>
</section>

{% include narrative-band.html band=site.cta_bands.research accent="sky" %}
