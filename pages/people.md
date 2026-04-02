---
layout: default
title: 团队成员
---

{% assign teacher_members = "" | split: "" %}
{% assign professor_members = site.data.team | where: "group_id", "professor" %}
{% assign associate_prof_members = site.data.team | where: "group_id", "associate_prof" %}
{% assign assistant_prof_members = site.data.team | where: "group_id", "assistant_prof" %}
{% assign teacher_members = teacher_members | concat: professor_members | concat: associate_prof_members | concat: assistant_prof_members %}

{% assign graduate_members = "" | split: "" %}
{% assign phd_members = site.data.team | where: "group_id", "phd" %}
{% assign master_members = site.data.team | where: "group_id", "master" %}
{% assign graduate_members = graduate_members | concat: phd_members | concat: master_members %}

{% assign other_members = "" | split: "" %}
{% assign researcher_members = site.data.team | where: "group_id", "researchers" %}
{% assign undergrad_members = site.data.team | where: "group_id", "undergrad" %}
{% assign intern_members = site.data.team | where: "group_id", "interns" %}
{% assign other_members = other_members | concat: researcher_members | concat: undergrad_members | concat: intern_members %}

{% assign alumni_members = site.data.team | where: "group_id", "alumni" %}

{% include page-header.html header=site.people_header accent="cyan" %}

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-14 md:py-18">
  <div class="grid gap-10 xl:grid-cols-[0.62fr_1.38fr] xl:items-start">
    {% include chapter-intro.html
      serial="PEOPLE"
      accent="sky"
      reveal="left"
      kicker_zh="团队地图"
      kicker_en="Team Atlas"
      title_zh="这页不只是成员列表，而是研究组织结构的可视化切面"
      title_en="This Page Is Not Just a Roster, but a Visible Slice of the Research Organization"
      description_zh="从教授、研究员到博士、硕士、本科与校友，每一组都代表不同的研究角色和协作方式。你可以先从团队结构看整体，再进入具体人物。"
      description_en="From professors and researchers to Ph.D. students, master students, undergraduates, and alumni, each group reflects a different role in the lab's research structure and collaboration model."
    %}

    <div class="exhibit-index" data-reveal="scale">
      {% if teacher_members.size > 0 %}
      <a href="#group-teachers" class="exhibit-index__item">
        <span class="exhibit-index__num">{{ teacher_members.size }}</span>
        <div class="min-w-0">
          <p class="text-lg font-black leading-tight text-slate-900 dark:text-white">
            <span class="lang-zh">老师</span>
            <span class="lang-en">Faculty</span>
          </p>
          <p class="mt-3 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
            <span class="lang-zh">教授、副教授和助理教授统一放在同一个栏目里，方便集中浏览核心教师团队。</span>
            <span class="lang-en">Professors, associate professors, and assistant professors are grouped together for a clearer faculty overview.</span>
          </p>
        </div>
      </a>
      {% endif %}

      {% if graduate_members.size > 0 %}
      <a href="#group-graduate-students" class="exhibit-index__item">
        <span class="exhibit-index__num">{{ graduate_members.size }}</span>
        <div class="min-w-0">
          <p class="text-lg font-black leading-tight text-slate-900 dark:text-white">
            <span class="lang-zh">博士与硕士</span>
            <span class="lang-en">Ph.D. & Master Students</span>
          </p>
          <p class="mt-3 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
            <span class="lang-zh">博士生和硕士生放在同一个栏目里，更贴近实验室日常培养与协作关系。</span>
            <span class="lang-en">Ph.D. and master students are placed in one section to better reflect everyday collaboration and mentorship.</span>
          </p>
        </div>
      </a>
      {% endif %}

      {% if other_members.size > 0 %}
      <a href="#group-others" class="exhibit-index__item">
        <span class="exhibit-index__num">{{ other_members.size }}</span>
        <div class="min-w-0">
          <p class="text-lg font-black leading-tight text-slate-900 dark:text-white">
            <span class="lang-zh">其他成员</span>
            <span class="lang-en">Other Members</span>
          </p>
          <p class="mt-3 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
            <span class="lang-zh">研究员、本科生和实习生集中展示，体现不同参与方式下的研究支持与系统协作。</span>
            <span class="lang-en">Researchers, undergraduates, and interns are grouped together to show broader participation in the lab's research and systems work.</span>
          </p>
        </div>
      </a>
      {% endif %}

      {% if alumni_members.size > 0 %}
      <a href="#group-alumni" class="exhibit-index__item">
        <span class="exhibit-index__num">{{ alumni_members.size }}</span>
        <div class="min-w-0">
          <p class="text-lg font-black leading-tight text-slate-900 dark:text-white">
            <span class="lang-zh">过往学生</span>
            <span class="lang-en">Alumni & Former Students</span>
          </p>
          <p class="mt-3 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
            <span class="lang-zh">校友区做得更大一些，突出实验室培养路径及其延展出去的学术与产业网络。</span>
            <span class="lang-en">The alumni section is given more presence to emphasize the lab's training path and the network it grows into.</span>
          </p>
        </div>
      </a>
      {% endif %}
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pb-8">
  <div class="space-y-12 md:space-y-14">
    {% if teacher_members.size > 0 %}
    {% include team-group-section.html
      section_id="group-teachers"
      serial="01"
      title_zh="老师"
      title_en="Faculty"
      description_zh="教授、副教授和助理教授统一放在这里，强调实验室核心教师团队的整体结构与研究判断。"
      description_en="Professors, associate professors, and assistant professors are presented together to emphasize the lab's core faculty structure and academic direction."
      color="indigo"
      layout="lead"
      members=teacher_members
    %}
    {% endif %}

    {% if graduate_members.size > 0 %}
    {% include team-group-section.html
      section_id="group-graduate-students"
      serial="02"
      title_zh="博士与硕士"
      title_en="Ph.D. & Master Students"
      description_zh="博士生和硕士生统一展示，更贴近实验室在项目推进、论文产出和日常协作中的真实结构。"
      description_en="Ph.D. and master students are shown together to better reflect how projects, papers, and daily collaboration actually unfold in the lab."
      color="blue"
      layout="compact"
      members=graduate_members
    %}
    {% endif %}

    {% if other_members.size > 0 %}
    {% include team-group-section.html
      section_id="group-others"
      serial="03"
      title_zh="其他成员"
      title_en="Other Members"
      description_zh="研究员、本科生和实习生共同组成实验室的重要支撑层，连接方向探索、系统实现与研究传播。"
      description_en="Researchers, undergraduates, and interns form an important support layer that connects exploration, implementation, and research communication."
      color="emerald"
      layout="compact"
      members=other_members
    %}
    {% endif %}

    {% if alumni_members.size > 0 %}
    {% include team-group-section.html
      section_id="group-alumni"
      serial="04"
      title_zh="过往学生"
      title_en="Alumni & Former Students"
      description_zh="校友区保留更大的展示体量，用来突出实验室培养路径，以及成员毕业后在学术界和产业界的延展去向。"
      description_en="The alumni section is intentionally larger so the page can better show the lab's training path and where former members continue in academia and industry."
      color="slate"
      layout="alumni_feature"
      members=alumni_members
    %}
    {% endif %}
  </div>
</section>

{% include narrative-band.html band=site.cta_bands.people accent="sky" %}
