---
layout: default
title: 首页
---

<section class="relative pt-24 pb-20 md:pb-32 overflow-hidden">
  <div class="absolute inset-0 bg-gradient-to-b from-slate-50 to-white -z-10"></div>
  <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMGg0MHY0MEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGQ9Ik0wIDM5LjVMMDQwIDM5LjUiIHN0cm9rZT0icmdiYSgwLCAwLCAwLCAwLjAzKSIgc3Ryb2tlLXdpZHRoPSIxIi8+PHBhdGggZD0iTTM5LjUgMEwzOS41IDQwIiBzdHJva2U9InJnYmEoMCwgMCwgMCwgMC4wMykiIHN0cm9rZS13aWR0aD0iMSIvPjwvc3ZnPg==')] opacity-50 -z-10"></div>
  <div class="absolute top-0 right-0 w-[40rem] h-[40rem] bg-blue-100 rounded-full blur-3xl opacity-40 -translate-y-1/2 translate-x-1/3 -z-10"></div>
  
  <div class="max-w-6xl mx-auto px-4 text-center">
    <div class="inline-block mb-6 px-5 py-2 rounded-full bg-white border border-blue-100 text-blue-600 text-sm font-bold tracking-wide shadow-sm hover:shadow-md transition-shadow">
      Tongji University · LV Research Group
    </div>
    <h1 class="text-5xl md:text-7xl font-extrabold text-slate-900 mb-8 tracking-tight leading-tight">
      探索物理世界的 <br class="hidden md:block" />
      <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500">3D感知与具身智能</span>
    </h1>
    <p class="text-xl md:text-2xl text-slate-500 mb-12 max-w-3xl mx-auto leading-relaxed font-light">
      致力于多模态感知、推理与交互的共性基础研究，探索空天智能与智能体在复杂真实世界中的前沿边界。
    </p>
    <div class="flex flex-col sm:flex-row justify-center items-center space-y-4 sm:space-y-0 sm:space-x-6 mb-16">
      <a href="{{ site.baseurl }}/pages/people.html" class="w-full sm:w-auto bg-blue-600 text-white px-10 py-4 rounded-2xl font-bold hover:bg-blue-700 hover:shadow-lg hover:shadow-blue-200 hover:-translate-y-1 transition-all duration-300">
        了解团队
      </a>
      <a href="{{ site.baseurl }}/research" class="w-full sm:w-auto bg-white border border-slate-200 text-slate-700 px-10 py-4 rounded-2xl font-bold hover:bg-slate-50 hover:shadow-sm transition-all duration-300">
        研究方向
      </a>
    </div>

    <div class="relative max-w-5xl mx-auto rounded-[2rem] overflow-hidden shadow-2xl border-4 border-white">
      <div class="absolute inset-0 bg-blue-900/10 mix-blend-multiply z-10"></div>
      <img src="https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=2000&auto=format&fit=crop" alt="LV Group Research Visual" class="w-full h-64 md:h-96 object-cover transform hover:scale-105 transition-transform duration-700">
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-20 border-t border-slate-100">
  <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-4">
      <div class="flex items-center space-x-4 border-l-4 border-cyan-500 pl-4">
          <div>
              <h2 class="text-3xl font-bold text-slate-800 tracking-tight">核心研究方向</h2>
              <span class="text-slate-400 font-light italic">Research Areas</span>
          </div>
      </div>
  </div>

  <div class="grid md:grid-cols-3 gap-8">
    {% for item in site.data.research %}
    <a href="{{ site.baseurl }}/research" class="group bg-white p-10 rounded-[2.5rem] shadow-sm border border-slate-100 hover:shadow-2xl hover:border-blue-100 hover:-translate-y-2 transition-all duration-500 flex flex-col h-full cursor-pointer">
      <div class="w-16 h-16 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center text-3xl mb-6 group-hover:bg-blue-600 group-hover:text-white transition-colors duration-300 shadow-sm">
        {{ item.icon }}
      </div>
      <h3 class="text-2xl font-bold mb-4 text-slate-900 group-hover:text-blue-600 transition-colors">{{ item.title }}</h3>
      <p class="text-slate-500 leading-relaxed flex-grow">{{ item.description }}</p>
      
      <div class="mt-6 pt-6 border-t border-slate-50 flex justify-end opacity-0 group-hover:opacity-100 transition-opacity duration-300">
         <span class="w-10 h-10 rounded-full bg-blue-50 flex items-center justify-center text-blue-600">
           <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
         </span>
      </div>
    </a>
    {% endfor %}
  </div>
</section>

<section class="bg-slate-50 py-20">
  <div class="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-12">
      
      <div>
          <div class="flex items-center space-x-4 mb-8 border-l-4 border-blue-600 pl-4">
              <h2 class="text-2xl font-bold text-slate-800 tracking-tight">最新动态</h2>
          </div>
          <div class="bg-white rounded-[2rem] p-8 border border-slate-100 shadow-sm h-full">
            <ul class="space-y-6">
              <li class="flex items-start gap-4 pb-6 border-b border-slate-50 last:border-0 last:pb-0">
                <span class="text-blue-600 font-bold shrink-0 w-20">2026.03</span>
                <p class="text-slate-600 leading-relaxed text-sm">
                  🎉 恭喜课题组新版主页正式上线！我们将在这里分享最新的学术成果与开源项目。
                </p>
              </li>
              <li class="flex items-start gap-4 pb-6 border-b border-slate-50 last:border-0 last:pb-0">
                <span class="text-slate-500 font-medium shrink-0 w-20">2026.01</span>
                <p class="text-slate-600 leading-relaxed text-sm">
                  🚀 课题组正式开源了基于多目标跟踪的 <span class="font-semibold text-slate-800">Unismot</span> 项目框架，支持 UniRTL 与 COCO 数据集，欢迎在 GitHub 体验。
                </p>
              </li>
              <li class="flex items-start gap-4">
                <span class="text-slate-500 font-medium shrink-0 w-20">2025.12</span>
                <p class="text-slate-600 leading-relaxed text-sm">
                  🏆 实验室成员荣获同济大学优秀科研奖励，并在国际顶级会议上进行成果汇报。
                </p>
              </li>
            </ul>
            <a href="{{ site.baseurl }}/news" class="mt-6 inline-block text-sm font-semibold text-blue-600 hover:text-blue-800 transition">查看所有新闻 &rarr;</a>
          </div>
      </div>

      <div>
          <div class="flex items-center space-x-4 mb-8 border-l-4 border-indigo-500 pl-4">
              <h2 class="text-2xl font-bold text-slate-800 tracking-tight">精选成果</h2>
          </div>
          <div class="bg-white rounded-[2rem] p-8 border border-slate-100 shadow-sm h-full flex flex-col justify-between">
              <div class="space-y-6">
                  <div class="group">
                      <span class="inline-block px-2 py-1 bg-indigo-50 text-indigo-600 text-xs font-bold rounded mb-2">CVPR 2026</span>
                      <h3 class="text-base font-bold text-slate-900 group-hover:text-blue-600 transition-colors leading-snug mb-1 cursor-pointer">
                          Towards Generalizable 3D Perception: A Novel Framework for Embodied Agents
                      </h3>
                      <p class="text-sm text-slate-500 italic line-clamp-1">Weiwei Guo, Wenbin Zuo, et al.</p>
                  </div>
                  <div class="group">
                      <span class="inline-block px-2 py-1 bg-indigo-50 text-indigo-600 text-xs font-bold rounded mb-2">NeurIPS 2025</span>
                      <h3 class="text-base font-bold text-slate-900 group-hover:text-blue-600 transition-colors leading-snug mb-1 cursor-pointer">
                          Unismot: Unified Single and Multiple Object Tracking in Complex Scenarios
                      </h3>
                      <p class="text-sm text-slate-500 italic line-clamp-1">Wenbin Zuo, Weiwei Guo, et al.</p>
                  </div>
              </div>
              <a href="{{ site.baseurl }}/publications" class="mt-8 inline-block text-sm font-semibold text-blue-600 hover:text-blue-800 transition">浏览所有论文 &rarr;</a>
          </div>
      </div>

  </div>
</section>