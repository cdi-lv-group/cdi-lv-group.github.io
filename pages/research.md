---
layout: default
title: 研究方向
---

{% comment %}
========================================================
页面：研究方向 (Research)
技术栈：Tailwind CSS + Jekyll Liquid
核心机制：
1. 暗黑模式：通过 `dark:` 前缀实现，例如 `bg-white dark:bg-slate-900`
2. 双语无缝切换：通过 `<span class="lang-zh">` 和 `<span class="lang-en">` 包裹，依赖 `default.html` 里的 CSS 动态隐藏/显示
3. 动画过渡：全局使用 `transition-colors duration-300` 让白天黑夜切换极其丝滑
========================================================
{% endcomment %}

<section class="bg-white dark:bg-slate-900 border-b border-slate-100 dark:border-slate-800 py-16 md:py-24 relative overflow-hidden z-0 transition-colors duration-300">
    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMGg0MHY0MEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGQ9Ik0wIDM5LjVMMDQwIDM5LjUiIHN0cm9rZT0icmdiYSgwLCAwLCAwLCAwLjAzKSIgc3Ryb2tlLXdpZHRoPSIxIi8+PHBhdGggZD0iTTM5LjUgMEwzOS41IDQwIiBzdHJva2U9InJnYmEoMCwgMCwgMCwgMC4wMykiIHN0cm9rZS13aWR0aD0iMSIvPjwvc3ZnPg==')] dark:opacity-[0.05] dark:invert opacity-40 -z-10 transition-opacity"></div>
    <div class="absolute top-0 right-0 w-[40rem] h-[40rem] bg-cyan-50 dark:bg-cyan-900/20 rounded-full blur-3xl opacity-60 -translate-y-1/2 translate-x-1/3 transition-colors duration-300 -z-10"></div>
    
    <div class="max-w-6xl mx-auto px-4 relative z-10 text-center md:text-left">
        <div class="inline-block mb-4 px-4 py-1.5 rounded-full bg-blue-50 dark:bg-slate-800 border border-blue-100 dark:border-blue-900 text-blue-600 dark:text-blue-400 text-sm font-bold tracking-wide shadow-sm transition-colors">
            <span class="lang-zh">研究方向</span>
            <span class="lang-en font-medium tracking-wider uppercase text-[10px]">Research Areas</span>
        </div>

        <h1 class="text-4xl md:text-6xl font-extrabold text-slate-900 dark:text-white mb-6 tracking-tight leading-tight transition-colors">
            <span class="lang-zh">探索智能的 <br class="hidden md:block" /> <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">物理边界</span></span>
            <span class="lang-en">Exploring the <br class="hidden md:block" /> <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">Physical Boundaries</span> of AI</span>
        </h1>

        <p class="text-lg md:text-xl text-slate-500 dark:text-slate-400 max-w-3xl leading-relaxed font-light mx-auto md:mx-0 transition-colors">
            <span class="lang-zh">我们致力于多模态感知、3D视觉与具身智能的基础理论与前沿应用研究，旨在让智能体在复杂、不确定的真实世界中具备强大的自主行为能力。</span>
            <span class="lang-en">We are dedicated to foundational theories and cutting-edge applications in multimodal perception, 3D vision, and embodied AI, aiming to equip agents with robust autonomous behaviors in complex, real-world environments.</span>
        </p>
    </div>
</section>


<section class="max-w-6xl mx-auto px-4 py-16 md:py-24">
    
    <div class="space-y-20">
        {% for area in site.data.research %}
        
        <div id="area-{{ forloop.index }}" class="group bg-white dark:bg-slate-800 rounded-[3rem] p-8 md:p-12 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-2xl transition-all duration-700 relative overflow-hidden flex flex-col {% cycle 'md:flex-row', 'md:flex-row-reverse' %} gap-10 lg:gap-16 items-center">
            
            <div class="absolute top-6 {% cycle 'right-10', 'left-10' %} text-[8rem] font-black text-slate-50 dark:text-slate-700/30 opacity-50 pointer-events-none select-none z-0 tracking-tighter transition-colors duration-300">
                0{{ forloop.index }}
            </div>

            <div class="absolute -bottom-10 {% cycle '-right-10', '-left-10' %} text-[15rem] opacity-5 group-hover:opacity-10 group-hover:scale-110 transition-all duration-700 pointer-events-none select-none z-0">
                {{ area.icon }}
            </div>

            <div class="flex-1 relative z-10 w-full">
                <div class="w-16 h-16 bg-gradient-to-br from-blue-50 to-cyan-50 dark:from-slate-700 dark:to-slate-600 text-blue-600 dark:text-blue-400 rounded-2xl flex items-center justify-center text-4xl mb-8 group-hover:scale-110 group-hover:shadow-lg group-hover:shadow-blue-100 dark:group-hover:shadow-blue-900/50 transition-all duration-500 border border-blue-100/50 dark:border-slate-500">
                    {{ area.icon }}
                </div>
                
                <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-6 tracking-tight transition-colors duration-300">
                    <span class="lang-zh">{{ area.title.zh | default: area.title }}</span>
                    <span class="lang-en">{{ area.title.en | default: area.title }}</span>
                </h2>
                
                <p class="text-lg text-slate-600 dark:text-slate-400 leading-relaxed mb-8 transition-colors duration-300">
                    <span class="lang-zh">{{ area.description.zh | default: area.description }}</span>
                    <span class="lang-en">{{ area.description.en | default: area.description }}</span>
                </p>
                
                {% if area.image %}
                <div class="mt-8 rounded-3xl overflow-hidden shadow-lg border border-slate-100 dark:border-slate-700 relative group/img transition-colors duration-300">
                    <div class="absolute inset-0 bg-blue-900/0 group-hover/img:bg-blue-900/10 transition-colors duration-500 z-10"></div>
                    <img src="{{ site.baseurl }}{{ area.image }}" alt="{{ area.title.zh | default: area.title }}" class="w-full h-64 md:h-80 object-cover transform group-hover/img:scale-105 transition-transform duration-700">
                </div>
                {% endif %}
            </div>

            <div class="w-full md:w-5/12 relative z-10 flex flex-col justify-center">
                <div class="bg-slate-50/80 dark:bg-slate-900/50 backdrop-blur-sm rounded-[2rem] p-8 md:p-10 border border-slate-100 dark:border-slate-700 group-hover:bg-blue-50/40 dark:group-hover:bg-slate-700/50 group-hover:border-blue-100 dark:group-hover:border-slate-600 transition-colors duration-500 shadow-sm">
                    <h3 class="text-xs font-black text-blue-600 dark:text-blue-400 uppercase tracking-widest mb-6 flex items-center gap-2 transition-colors duration-300">
                        <span class="w-2 h-2 rounded-full bg-blue-500 dark:bg-blue-400"></span> 
                        <span class="lang-zh">核心关注领域 (Focus Areas)</span>
                        <span class="lang-en">Key Focus Areas</span>
                    </h3>
                    
                    {% comment %} 
                      【复杂列表数据兜底机制】
                      对于 YAML 数组 (points)，我们不能像字符串那样直接 default。
                      因此先进行变量赋值：如果存在 points.zh 就用，不存在就用旧的 points 数组。
                    {% endcomment %}
                    {% assign points_zh = area.points.zh | default: area.points %}
                    {% assign points_en = area.points.en | default: area.points %}
                    
                    <ul class="space-y-6 lang-zh">
                        {% for point in points_zh %}
                        <li class="group/item flex items-start text-slate-700 dark:text-slate-300 hover:text-blue-700 dark:hover:text-blue-400 transition-colors">
                            <span class="flex-shrink-0 w-7 h-7 rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-600 text-blue-500 dark:text-blue-400 flex items-center justify-center mt-0.5 mr-4 group-hover/item:bg-blue-600 group-hover/item:text-white dark:group-hover/item:bg-blue-500 dark:group-hover/item:text-white group-hover/item:border-blue-600 dark:group-hover/item:border-blue-500 group-hover/item:scale-110 transition-all duration-300 shadow-sm">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
                            </span>
                            <span class="leading-relaxed font-medium group-hover/item:translate-x-1 transition-transform duration-300">{{ point }}</span>
                        </li>
                        {% endfor %}
                    </ul>

                    <ul class="space-y-6 lang-en">
                        {% for point in points_en %}
                        <li class="group/item flex items-start text-slate-700 dark:text-slate-300 hover:text-blue-700 dark:hover:text-blue-400 transition-colors">
                            <span class="flex-shrink-0 w-7 h-7 rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-600 text-blue-500 dark:text-blue-400 flex items-center justify-center mt-0.5 mr-4 group-hover/item:bg-blue-600 group-hover/item:text-white dark:group-hover/item:bg-blue-500 dark:group-hover/item:text-white group-hover/item:border-blue-600 dark:group-hover/item:border-blue-500 group-hover/item:scale-110 transition-all duration-300 shadow-sm">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
                            </span>
                            <span class="leading-relaxed font-medium group-hover/item:translate-x-1 transition-transform duration-300">{{ point }}</span>
                        </li>
                        {% endfor %}
                    </ul>
                </div>
            </div>

        </div>
        {% endfor %}
    </div>

</section>

<section class="py-20 mt-10 relative overflow-hidden transition-colors duration-500 bg-white dark:bg-slate-950">
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full bg-gradient-to-b from-blue-50/50 to-transparent dark:from-blue-900/10 dark:to-transparent pointer-events-none -z-10"></div>
    <div class="absolute -top-24 -right-24 w-96 h-96 bg-cyan-100/40 dark:bg-cyan-900/10 rounded-full blur-[100px] pointer-events-none -z-10"></div>

    <div class="max-w-5xl mx-auto px-4 relative z-10">
        <div class="relative bg-white/60 dark:bg-slate-900/40 backdrop-blur-xl rounded-[3rem] p-10 md:p-20 border border-blue-100 dark:border-slate-800 shadow-sm dark:shadow-none text-center transition-all duration-300">
            
            <div class="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-blue-600 text-white mb-8 shadow-lg shadow-blue-200 dark:shadow-none">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path>
                </svg>
            </div>

            <h2 class="text-3xl md:text-5xl font-black text-slate-900 dark:text-white mb-6 tracking-tight leading-tight">
                <span class="lang-zh">
                    了解我们在这些领域的 <br class="md:hidden" />
                    <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">最新科研成果</span>
                </span>
                <span class="lang-en">
                    Discover Our <br class="md:hidden" />
                    <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">Latest Achievements</span>
                </span>
            </h2>
            
            <p class="text-slate-500 dark:text-slate-400 mb-12 text-lg md:text-xl max-w-2xl mx-auto font-normal leading-relaxed">
                <span class="lang-zh">我们的研究成果常年发表于 <span class="text-blue-600 dark:text-blue-400 font-bold">CVPR, ICCV, ECCV, NeurIPS</span> 等国际顶级会议。代码与模型均同步开源。</span>
                <span class="lang-en">Regularly published in <span class="text-blue-600 dark:text-blue-400 font-bold">CVPR, ICCV, ECCV, and NeurIPS</span>. All codes and models are open-sourced.</span>
            </p>
            
            <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                <a href="{{ site.baseurl }}/pages/publications.html" 
                   class="w-full sm:w-auto inline-flex items-center justify-center group bg-blue-600 hover:bg-blue-700 text-white px-10 py-4 rounded-2xl font-bold transition-all shadow-xl shadow-blue-100 dark:shadow-none hover:-translate-y-1">
                    <span class="lang-zh">查看学术成果</span>
                    <span class="lang-en">View Publications</span>
                    <svg class="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path>
                    </svg>
                </a>
                
                <a href="https://github.com/{{ site.github_username }}" target="_blank"
                   class="w-full sm:w-auto inline-flex items-center justify-center px-10 py-4 rounded-2xl font-bold text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 transition-all">
                    <span class="lang-zh">开源代码库</span>
                    <span class="lang-en">GitHub Repos</span>
                </a>
            </div>
        </div>
    </div>
</section>