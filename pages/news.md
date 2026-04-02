---
layout: default
title: 新闻动态
---

{% assign featured_news = site.data.news | first %}
{% include page-header.html header=site.news_header accent="cyan" %}

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-14 md:py-20">
  <div class="stage-shell px-6 py-8 md:px-10 md:py-10" data-stage="featured-news" data-reveal="scale">
    <div class="grid gap-8 xl:grid-cols-[1.02fr_0.98fr] xl:items-end">
      <div>
        <p class="section-kicker text-[0.72rem] font-black uppercase text-sky-600 dark:text-cyan-300">
          <span class="lang-zh">动态主舞台</span>
          <span class="lang-en">Featured Update Stage</span>
        </p>

        <h2 class="mt-4 text-3xl font-black leading-tight text-slate-900 dark:text-white md:text-5xl">
          <span class="lang-zh">把实验室最近发生的关键变化先展示在最前面</span>
          <span class="lang-en">Put the Lab's Most Important Recent Shift Right at the Front</span>
        </h2>

        <p class="mt-5 max-w-3xl text-base leading-relaxed text-slate-600 dark:text-slate-300 md:text-lg">
          <span class="lang-zh">新闻页延续首页的展陈逻辑：先给出一个主动态作为阅读锚点，再把其余事件放进沿时间展开的章节里，帮助访问者快速掌握实验室的节奏。</span>
          <span class="lang-en">The news page extends the same exhibition logic as the homepage: start with a featured milestone, then unfold the remaining events through a time-based sequence that makes the lab's rhythm easier to understand.</span>
        </p>
      </div>

      <div class="panel-surface p-5 md:p-6">
        <p class="section-kicker text-[0.68rem] font-black uppercase text-slate-400 dark:text-slate-500">
          <span class="lang-zh">当前锚点</span>
          <span class="lang-en">Current Anchor</span>
        </p>
        <p class="mt-3 text-sm font-black uppercase tracking-[0.18em] text-slate-400 dark:text-slate-500">{{ featured_news.date }}</p>
        <p class="mt-3 text-xl font-black leading-snug text-slate-900 dark:text-white">
          <span class="lang-zh">{{ featured_news.title.zh }}</span>
          <span class="lang-en">{{ featured_news.title.en }}</span>
        </p>
        <p class="mt-4 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
          <span class="lang-zh">{{ featured_news.category.zh }}</span>
          <span class="lang-en">{{ featured_news.category.en }}</span>
        </p>
      </div>
    </div>

    <div class="mt-8 grid gap-6 xl:grid-cols-[1.05fr_0.95fr] xl:items-end">
      {% include news-card.html
        item=featured_news
        variant="feature"
        outer_class="p-6 md:p-8"
        show_button=true
      %}

      <div class="grid gap-5">
        {% for item in site.data.news offset:1 limit:3 %}
        {% include news-card.html
          item=item
          variant="summary"
          outer_class="p-5"
        %}
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pb-8">
  <div class="grid gap-10 xl:grid-cols-[0.58fr_1.42fr] xl:items-start">
    {% include chapter-intro.html
      serial="TIMELINE"
      accent="sky"
      reveal="left"
      kicker_zh="时间线章节"
      kicker_en="Timeline Chapters"
      title_zh="其余动态以轻量章节继续向下展开"
      title_en="The Rest of the Story Continues as Lightweight Time Chapters"
      description_zh="这里保留时间感，但不再依赖旧式居中时间轴。每条动态都作为一个清晰可读的章节卡出现，适配长标题和双语描述。"
      description_en="Time remains visible here, but the page no longer depends on the older centered timeline. Each update appears as a readable chapter card that handles long bilingual titles and descriptions more gracefully."
    %}

    <div class="space-y-5" data-reveal="right">
      {% for item in site.data.news offset:1 %}
      {% include news-card.html
        item=item
        variant="timeline"
        outer_class="p-5 md:p-6"
        show_button=true
      %}
      {% endfor %}
    </div>
  </div>
</section>

{% include narrative-band.html band=site.cta_bands.news accent="sky" %}
