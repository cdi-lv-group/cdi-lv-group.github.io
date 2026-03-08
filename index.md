---
layout: default
title: 首页
---

<section class="relative pt-24 pb-32 overflow-hidden">
  <div class="absolute inset-0 bg-gradient-to-b from-slate-50 to-white -z-10"></div>
  <div class="absolute top-0 right-0 w-[40rem] h-[40rem] bg-blue-50 rounded-full blur-3xl opacity-50 -translate-y-1/2 translate-x-1/3 -z-10"></div>
  
  <div class="max-w-6xl mx-auto px-4 text-center">
    <div class="inline-block mb-4 px-4 py-1.5 rounded-full bg-blue-50 border border-blue-100 text-blue-600 text-sm font-semibold tracking-wide shadow-sm">
      Tongji University · LV Research Group
    </div>
    <h1 class="text-5xl md:text-7xl font-extrabold text-slate-900 mb-8 tracking-tight">
      专注于 <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500">3D感知与具身智能</span>
    </h1>
    <p class="text-xl md:text-2xl text-slate-500 mb-12 max-w-3xl mx-auto leading-relaxed font-light">
      致力于多模态感知、推理与交互的共性基础研究，探索空天智能与智能体在复杂真实世界中的前沿边界。
    </p>
    <div class="flex flex-col sm:flex-row justify-center items-center space-y-4 sm:space-y-0 sm:space-x-6">
      <a href="{{ site.baseurl }}/pages/people.html" class="w-full sm:w-auto bg-blue-600 text-white px-10 py-4 rounded-2xl font-bold hover:bg-blue-700 hover:shadow-lg hover:shadow-blue-200 hover:-translate-y-1 transition-all duration-300">
        了解团队
      </a>
      <a href="{{ site.baseurl }}/research" class="w-full sm:w-auto bg-white border border-slate-200 text-slate-700 px-10 py-4 rounded-2xl font-bold hover:bg-slate-50 hover:shadow-sm transition-all duration-300">
        研究方向
      </a>
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-12">
  <div class="flex items-center space-x-4 mb-10 border-l-4 border-blue-600 pl-4">
      <h2 class="text-2xl font-bold text-slate-800 uppercase tracking-wide">最新动态</h2>
      <span class="text-slate-400 font-light italic">News & Highlights</span>
  </div>
  
  <div class="bg-white rounded-3xl p-8 border border-slate-100 shadow-sm">
    <ul class="space-y-6">
      <li class="flex flex-col md:flex-row md:items-start gap-4 pb-6 border-b border-slate-50 last:border-0 last:pb-0">
        <span class="text-blue-600 font-bold shrink-0 md:w-32">2026.03</span>
        <p class="text-slate-600 leading-relaxed">
          🎉 恭喜课题组新版主页正式上线！我们将在这里分享最新的学术成果与开源项目。
        </p>
      </li>
      <li class="flex flex-col md:flex-row md:items-start gap-4 pb-6 border-b border-slate-50 last:border-0 last:pb-0">
        <span class="text-slate-500 font-medium shrink-0 md:w-32">2026.01</span>
        <p class="text-slate-600 leading-relaxed">
          🔥 课题组在 <span class="font-semibold text-slate-800">计算机视觉与多模态感知</span> 领域取得新进展，相关开源框架已在 GitHub 发布，欢迎关注。
        </p>
      </li>
      <li class="flex flex-col md:flex-row md:items-start gap-4">
        <span class="text-slate-500 font-medium shrink-0 md:w-32">2025.12</span>
        <p class="text-slate-600 leading-relaxed">
          🏆 实验室成员荣获同济大学优秀科研奖励，并在国际顶级会议上进行汇报。
        </p>
      </li>
    </ul>
    <div class="mt-8 text-right">
      <a href="{{ site.baseurl }}/news" class="text-sm font-semibold text-blue-600 hover:text-blue-800 flex items-center justify-end gap-1 transition">
        查看所有新闻 <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
      </a>
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-16">
  <div class="flex items-center space-x-4 mb-10 border-l-4 border-cyan-500 pl-4">
      <h2 class="text-2xl font-bold text-slate-800 uppercase tracking-wide">核心研究方向</h2>
      <span class="text-slate-400 font-light italic">Research Areas</span>
  </div>

  <div class="grid md:grid-cols-3 gap-8">
    {% for item in site.data.research %}
    <div class="group bg-white p-10 rounded-[2.5rem] shadow-sm border border-slate-100 hover:shadow-2xl hover:-translate-y-2 transition-all duration-500 flex flex-col h-full">
      <div class="w-16 h-16 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center text-3xl mb-6 group-hover:bg-blue-600 group-hover:text-white transition-colors duration-300">
        {{ item.icon }}
      </div>
      <h3 class="text-2xl font-bold mb-4 text-slate-900">{{ item.title }}</h3>
      <p class="text-slate-500 leading-relaxed flex-grow">{{ item.description }}</p>
      
      <div class="mt-6 pt-6 border-t border-slate-50 flex justify-end opacity-0 group-hover:opacity-100 transition-opacity duration-300">
         <span class="w-10 h-10 rounded-full bg-slate-50 flex items-center justify-center text-blue-600">
           <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
         </span>
      </div>
    </div>
    {% endfor %}
  </div>
</section>