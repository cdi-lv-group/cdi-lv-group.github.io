---
layout: default
title: 首页
---

<section class="relative pt-24 pb-20 md:pb-32 overflow-hidden">
  <div class="absolute inset-0 bg-gradient-to-b from-slate-50 to-white dark:from-slate-900 dark:to-slate-900 transition-colors duration-300 -z-10"></div>
  
  <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMGg0MHY0MEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGQ9Ik0wIDM5LjVMMDQwIDM5LjUiIHN0cm9rZT0icmdiYSgwLCAwLCAwLCAwLjAzKSIgc3Ryb2tlLXdpZHRoPSIxIi8+PHBhdGggZD0iTTM5LjUgMEwzOS41IDQwIiBzdHJva2U9InJnYmEoMCwgMCwgMCwgMC4wMykiIHN0cm9rZS13aWR0aD0iMSIvPjwvc3ZnPg==')] opacity-50 dark:opacity-10 dark:invert transition-all duration-300 -z-10"></div>
  
  <div class="absolute top-0 right-0 w-[40rem] h-[40rem] bg-blue-100 dark:bg-blue-900/30 rounded-full blur-3xl opacity-40 -translate-y-1/2 translate-x-1/3 transition-colors duration-300 -z-10"></div>
  
  <div class="max-w-6xl mx-auto px-4 text-center">
    <div class="inline-block mb-6 px-5 py-2 rounded-full bg-white dark:bg-slate-800 border border-blue-100 dark:border-blue-900 text-blue-600 dark:text-blue-400 text-sm font-bold tracking-wide shadow-sm hover:shadow-md transition-shadow">
      Tongji University · LV Research Group
    </div>
    
    <h1 class="text-5xl md:text-7xl font-extrabold text-slate-900 dark:text-white mb-8 tracking-tight leading-tight transition-colors duration-300">
      探索物理世界的 <br class="hidden md:block" />
      <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">3D感知与具身智能</span>
    </h1>
    
    <p class="text-xl md:text-2xl text-slate-500 dark:text-slate-400 mb-12 max-w-3xl mx-auto leading-relaxed font-light transition-colors duration-300">
      致力于多模态感知、推理与交互的共性基础研究，探索空天智能与智能体在复杂真实世界中的前沿边界。
    </p>
    
    <div class="flex flex-col sm:flex-row justify-center items-center space-y-4 sm:space-y-0 sm:space-x-6 mb-16">
      <a href="{{ site.baseurl }}/pages/people.html" class="w-full sm:w-auto bg-blue-600 dark:bg-blue-600 text-white px-10 py-4 rounded-2xl font-bold hover:bg-blue-700 dark:hover:bg-blue-500 hover:shadow-lg hover:shadow-blue-200 dark:hover:shadow-blue-900 hover:-translate-y-1 transition-all duration-300">
        了解团队
      </a>
      <a href="{{ site.baseurl }}/pages/research.html" class="w-full sm:w-auto bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 px-10 py-4 rounded-2xl font-bold hover:bg-slate-50 dark:hover:bg-slate-700 hover:shadow-sm transition-all duration-300">
        研究方向
      </a>
    </div>

    <div class="relative max-w-5xl mx-auto rounded-[2rem] overflow-hidden shadow-2xl border-4 border-white dark:border-slate-800 transition-colors duration-300">
      <div class="absolute inset-0 bg-blue-900/10 mix-blend-multiply z-10"></div>
      <img src="https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=2000&auto=format&fit=crop" alt="LV Group Research Visual" class="w-full h-64 md:h-96 object-cover transform hover:scale-105 transition-transform duration-700">
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-20 border-t border-slate-100 dark:border-slate-800 transition-colors duration-300">
  <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-4">
      <div class="flex items-center space-x-4 border-l-4 border-cyan-500 pl-4">
          <div>
              <h2 class="text-3xl font-bold text-slate-800 dark:text-white tracking-tight transition-colors duration-300">核心研究方向</h2>
              <span class="text-slate-400 dark:text-slate-500 font-light italic transition-colors duration-300">Research Areas</span>
          </div>
      </div>
  </div>

  <div class="grid md:grid-cols-3 gap-8">
    {% for item in site.data.research %}
    <a href="{{ site.baseurl }}/pages/research.html" class="group bg-white dark:bg-slate-800 p-10 rounded-[2.5rem] shadow-sm border border-slate-100 dark:border-slate-700 hover:shadow-2xl hover:border-blue-100 dark:hover:border-blue-500 hover:-translate-y-2 transition-all duration-500 flex flex-col h-full cursor-pointer">
      
      <div class="w-16 h-16 bg-blue-50 dark:bg-slate-700 text-blue-600 dark:text-blue-400 rounded-2xl flex items-center justify-center text-3xl mb-6 group-hover:bg-blue-600 group-hover:text-white dark:group-hover:bg-blue-500 transition-colors duration-300 shadow-sm">
        {{ item.icon }}
      </div>
      
      <h3 class="text-2xl font-bold mb-4 text-slate-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors duration-300">{{ item.title }}</h3>
      <p class="text-slate-500 dark:text-slate-400 leading-relaxed flex-grow transition-colors duration-300">{{ item.description }}</p>
      
      <div class="mt-6 pt-6 border-t border-slate-50 dark:border-slate-700 flex justify-end opacity-0 group-hover:opacity-100 transition-opacity duration-300">
         <span class="w-10 h-10 rounded-full bg-blue-50 dark:bg-slate-700 flex items-center justify-center text-blue-600 dark:text-blue-400">
           <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
         </span>
      </div>
    </a>
    {% endfor %}
  </div>
</section>

<section class="bg-slate-50 dark:bg-slate-900 py-20 transition-colors duration-300">
  <div class="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-12">
      
      <div>
          <div class="flex items-center space-x-4 mb-8 border-l-4 border-blue-600 pl-4">
              <h2 class="text-2xl font-bold text-slate-800 dark:text-white tracking-tight transition-colors duration-300">最新动态</h2>
          </div>
          
          <div class="bg-white dark:bg-slate-800 rounded-[2rem] p-8 border border-slate-100 dark:border-slate-700 shadow-sm h-full flex flex-col transition-colors duration-300">
            <ul class="space-y-6 flex-grow">
              {% for item in site.data.news limit:3 %}
              <li class="flex items-start gap-4 pb-6 border-b border-slate-50 dark:border-slate-700/50 last:border-0 last:pb-0">
                <span class="text-blue-600 dark:text-blue-400 font-bold shrink-0 w-20 pt-0.5">{{ item.date }}</span>
                <div class="flex-1">
                  <a href="{% if item.link and item.link != '#' %}{{ item.link }}{% else %}{{ site.baseurl }}/pages/news.html{% endif %}" class="font-bold text-slate-800 dark:text-slate-200 hover:text-blue-600 dark:hover:text-blue-400 transition-colors block mb-1 text-sm leading-snug">
                    {{ item.title }}
                  </a>
                  <p class="text-slate-500 dark:text-slate-400 leading-relaxed text-xs line-clamp-2 transition-colors duration-300">
                    {{ item.description }}
                  </p>
                </div>
              </li>
              {% endfor %}
            </ul>
            <a href="{{ site.baseurl }}/pages/news.html" class="mt-6 inline-block text-sm font-semibold text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 transition-colors">查看所有新闻 &rarr;</a>
          </div>
      </div>

      <div>
          <div class="flex items-center space-x-4 mb-8 border-l-4 border-indigo-500 dark:border-indigo-400 pl-4">
              <h2 class="text-2xl font-bold text-slate-800 dark:text-white tracking-tight transition-colors duration-300">精选成果</h2>
          </div>
          
          <div class="bg-white dark:bg-slate-800 rounded-[2rem] p-8 border border-slate-100 dark:border-slate-700 shadow-sm h-full flex flex-col justify-between transition-colors duration-300">
              <div class="space-y-6 flex-grow">
                  {% for paper in site.data.publications limit:3 %}
                  <div class="group border-b border-slate-50 dark:border-slate-700/50 pb-5 last:border-0 last:pb-0">
                      
                      <div class="flex items-center gap-2 mb-2">
                          <span class="inline-block px-2 py-0.5 bg-indigo-50 dark:bg-indigo-900/40 text-indigo-600 dark:text-indigo-300 text-xs font-bold rounded">
                              {{ paper.venue }}
                          </span>
                          {% if paper.highlight %}
                          <span class="inline-block px-2 py-0.5 bg-red-50 dark:bg-red-900/40 text-red-600 dark:text-red-300 text-[0.65rem] font-bold rounded uppercase">
                              🔥 {{ paper.highlight }}
                          </span>
                          {% endif %}
                      </div>
                      
                      <h3 class="text-sm font-bold text-slate-900 dark:text-slate-200 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors leading-snug mb-1">
                          <a href="{% if paper.links.paper %}{{ paper.links.paper }}{% else %}{{ site.baseurl }}/pages/publications.html{% endif %}" target="_blank">
                              {{ paper.title }}
                          </a>
                      </h3>
                      
                      <p class="text-xs text-slate-500 dark:text-slate-400 italic line-clamp-1 transition-colors duration-300">{{ paper.authors }}</p>
                  </div>
                  {% endfor %}
              </div>
              <a href="{{ site.baseurl }}/pages/publications.html" class="mt-6 inline-block text-sm font-semibold text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 transition-colors">浏览所有论文 &rarr;</a>
          </div>
      </div>

  </div>
</section>