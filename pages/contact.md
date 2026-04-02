---
layout: default
title: 联系加入
---

{% include page-header.html header=site.join_header accent="sky" pulse=true inject_group_name=true %}

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-14 md:py-20">
  <div class="grid gap-10 xl:grid-cols-[0.6fr_1.4fr] xl:items-start">
    {% include chapter-intro.html
      serial="OPEN"
      accent="sky"
      reveal="left"
      kicker_zh="岗位机会"
      kicker_en="Open Positions"
      title_zh="从核心博士方向到研究运营支持，机会按角色层次展开"
      title_en="From Core Ph.D. Roles to Research Operations Support"
      description_zh="这不是一组简单的信息卡，而是一条从高强度研究岗位到系统支持岗位的机会序列。你可以先看最核心的主舞台岗位，再浏览其余方向。"
      description_en="This is not just a set of information cards. It is an opportunity sequence that spans high-intensity research roles and support roles. Start with the main-stage opening, then browse the rest."
    %}

    <div class="grid gap-6 xl:grid-cols-[1.06fr_0.94fr]">
      {% for position in site.data.positions limit:1 %}
      {% include position-card.html
        position=position
        variant="feature"
        outer_class="px-6 py-7 md:px-8 md:py-8"
        reveal="scale"
        stage="featured-position"
      %}
      {% endfor %}

      <div class="grid gap-5 sm:grid-cols-2" data-reveal="right">
        {% for position in site.data.positions offset:1 %}
        {% include position-card.html
          position=position
          variant="summary"
          outer_class="p-5"
        %}
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-10 md:py-14">
  <div class="grid gap-10 xl:grid-cols-[0.6fr_1.4fr] xl:items-start">
    {% include chapter-intro.html
      serial="PROOF"
      accent="sky"
      reveal="left"
      kicker_zh="为什么加入我们"
      kicker_en="Why Join Us"
      title_zh="把团队的说服力做成可被快速感知的信誉层"
      title_en="Turn Team Strength into a Readable Layer of Credibility"
      description_zh="我们希望申请者能在很短时间里感受到：这里不仅有方向，也有算力、指导、国际交流和真正能落地的研究系统。"
      description_en="Applicants should quickly understand that this lab offers not only strong directions, but also compute, mentorship, international exposure, and systems that turn ideas into real work."
    %}

    <div class="grid gap-5 md:grid-cols-3" data-reveal="scale">
      <article class="proof-card p-6 md:p-7">
        <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-sky-50 text-sky-600 dark:bg-slate-800 dark:text-cyan-300">
          <svg class="h-8 w-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path>
          </svg>
        </div>
        <h3 class="mt-6 text-2xl font-black leading-tight text-slate-900 dark:text-white">
          <span class="lang-zh">充足算力与实验支持</span>
          <span class="lang-en">Compute and Experiment Support</span>
        </h3>
        <p class="mt-4 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
          <span class="lang-zh">大规模 GPU 算力、实验平台和数据支持并行推进，减少研究推进过程中的基础设施阻力。</span>
          <span class="lang-en">Large-scale GPU access, experiment platforms, and data support move in parallel to reduce infrastructure drag during research execution.</span>
        </p>
      </article>

      <article class="proof-card p-6 md:p-7">
        <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-50 text-cyan-600 dark:bg-cyan-900/20 dark:text-cyan-300">
          <svg class="h-8 w-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path>
          </svg>
        </div>
        <h3 class="mt-6 text-2xl font-black leading-tight text-slate-900 dark:text-white">
          <span class="lang-zh">近距离指导与协作反馈</span>
          <span class="lang-en">Close Mentorship and Iterative Feedback</span>
        </h3>
        <p class="mt-4 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
          <span class="lang-zh">我们强调研究判断、系统实现和表达能力一起成长，鼓励从 idea 到实验到写作的完整闭环。</span>
          <span class="lang-en">We care about research judgment, system execution, and communication together, and encourage a full loop from idea to experiment to writing.</span>
        </p>
      </article>

      <article class="proof-card p-6 md:p-7">
        <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-emerald-50 text-emerald-600 dark:bg-emerald-900/20 dark:text-emerald-300">
          <svg class="h-8 w-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
        </div>
        <h3 class="mt-6 text-2xl font-black leading-tight text-slate-900 dark:text-white">
          <span class="lang-zh">国际合作与开放生态</span>
          <span class="lang-en">Global Collaboration and Open Ecosystems</span>
        </h3>
        <p class="mt-4 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
          <span class="lang-zh">研究成果面向国际顶会、开放代码与跨机构合作，帮助成员更早进入真实学术与系统生态。</span>
          <span class="lang-en">Work is oriented toward top venues, open-source releases, and cross-institution collaboration so members can enter real academic and systems ecosystems earlier.</span>
        </p>
      </article>
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-10 md:py-14">
  <div class="grid gap-10 xl:grid-cols-[0.58fr_1.42fr] xl:items-start">
    {% include chapter-intro.html
      serial="APPLY"
      accent="sky"
      reveal="left"
      kicker_zh="如何申请"
      kicker_en="Application Steps"
      title_zh="把表达兴趣这件事，变成一条清晰而高质量的进入路径"
      title_en="Turn Interest into a Clear, High-Quality Entry Path"
      description_zh="我们更希望看到的是研究判断、执行潜力和真实投入意愿。下面这组步骤，会帮助你把联系邮件写得更具体，也更容易让双方快速判断匹配度。"
      description_en="We care more about research judgment, execution potential, and genuine commitment. These steps help you make first contact more concrete so both sides can quickly evaluate fit."
    %}

    <div class="grid gap-6 xl:grid-cols-[1.06fr_0.94fr]">
      <div class="grid gap-5 md:grid-cols-3">
        {% for step in site.join_process.steps %}
        <article class="position-card p-5 md:p-6" data-reveal="scale">
          <span class="exhibit-index__num">0{{ forloop.index }}</span>
          <h3 class="mt-5 text-xl font-black leading-tight text-slate-900 dark:text-white">
            <span class="lang-zh">{{ step.title.zh }}</span>
            <span class="lang-en">{{ step.title.en }}</span>
          </h3>
          <p class="mt-4 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
            <span class="lang-zh">{{ step.description.zh }}</span>
            <span class="lang-en">{{ step.description.en }}</span>
          </p>
        </article>
        {% endfor %}
      </div>

      <div class="grid gap-5" data-reveal="right">
        <div class="stage-rail p-6 md:p-7">
          <p class="section-kicker text-[0.68rem] font-black uppercase text-sky-600 dark:text-cyan-300">
            <span class="lang-zh">{{ site.join_process.subject_label.zh }}</span>
            <span class="lang-en">{{ site.join_process.subject_label.en }}</span>
          </p>
          <code class="mt-4 block text-sm font-medium leading-relaxed text-slate-700 dark:text-slate-100 break-all">
            <span class="lang-zh">{{ site.join_process.subject_value.zh }}</span>
            <span class="lang-en">{{ site.join_process.subject_value.en }}</span>
          </code>
        </div>

        <div class="panel-surface p-6 md:p-7">
          <p class="section-kicker text-[0.68rem] font-black uppercase text-slate-400 dark:text-slate-500">
            <span class="lang-zh">{{ site.join_process.contact_label.zh }}</span>
            <span class="lang-en">{{ site.join_process.contact_label.en }}</span>
          </p>
          <a href="mailto:{{ site.lab.email }}" class="mt-4 inline-flex items-center rounded-full border border-slate-200/90 bg-white/75 px-4 py-2 text-sm font-black text-sky-600 transition-colors hover:border-sky-300 hover:text-sky-700 dark:border-slate-700 dark:bg-slate-900/70 dark:text-cyan-300 dark:hover:border-cyan-400 dark:hover:text-cyan-200">{{ site.lab.email }}</a>
          <p class="mt-4 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
            <span class="lang-zh">{{ site.join_process.contact_value.zh }}</span>
            <span class="lang-en">{{ site.join_process.contact_value.en }}</span>
          </p>

          <p class="mt-6 text-xs font-black uppercase tracking-[0.18em] text-slate-400 dark:text-slate-500">
            <span class="lang-zh">{{ site.join_process.response_label.zh }}</span>
            <span class="lang-en">{{ site.join_process.response_label.en }}</span>
          </p>
          <p class="mt-3 text-sm leading-relaxed text-slate-600 dark:text-slate-300">
            <span class="lang-zh">{{ site.join_process.response_value.zh }}</span>
            <span class="lang-en">{{ site.join_process.response_value.en }}</span>
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

{% include narrative-band.html band=site.cta_bands.join accent="sky" %}
