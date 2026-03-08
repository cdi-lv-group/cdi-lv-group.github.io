---
layout: default
title: 研究方向
---

<section class="bg-white border-b border-slate-100 py-16 md:py-24 relative overflow-hidden z-0">
    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMGg0MHY0MEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGQ9Ik0wIDM5LjVMMDQwIDM5LjUiIHN0cm9rZT0icmdiYSgwLCAwLCAwLCAwLjAzKSIgc3Ryb2tlLXdpZHRoPSIxIi8+PHBhdGggZD0iTTM5LjUgMEwzOS41IDQwIiBzdHJva2U9InJnYmEoMCwgMCwgMCwgMC4wMykiIHN0cm9rZS13aWR0aD0iMSIvPjwvc3ZnPg==')] opacity-60 -z-10"></div>
    <div class="absolute top-0 right-0 w-[40rem] h-[40rem] bg-cyan-50 rounded-full blur-3xl opacity-60 -translate-y-1/2 translate-x-1/3 -z-10"></div>
    <div class="absolute bottom-0 left-0 w-[30rem] h-[30rem] bg-blue-50 rounded-full blur-3xl opacity-40 translate-y-1/3 -translate-x-1/3 -z-10"></div>
    
    <div class="max-w-6xl mx-auto px-4 relative z-10 text-center md:text-left">
        <div class="inline-block mb-4 px-4 py-1.5 rounded-full bg-blue-50 border border-blue-100 text-blue-600 text-sm font-bold tracking-wide shadow-sm">
            Research Areas
        </div>
        <h1 class="text-4xl md:text-6xl font-extrabold text-slate-900 mb-6 tracking-tight leading-tight">
            探索智能的 <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500">物理边界</span>
        </h1>
        <p class="text-lg md:text-xl text-slate-500 max-w-3xl leading-relaxed font-light mx-auto md:mx-0">
            我们致力于多模态感知、3D视觉与具身智能的基础理论与前沿应用研究，旨在让智能体在复杂、不确定的真实世界中具备强大的自主行为能力。
        </p>
    </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-16 md:py-24">
    
    <div class="space-y-20">
        {% for area in site.data.research %}
        
        <div id="area-{{ forloop.index }}" class="group bg-white rounded-[3rem] p-8 md:p-12 border border-slate-100 shadow-sm hover:shadow-2xl transition-all duration-700 relative overflow-hidden flex flex-col {% cycle 'md:flex-row', 'md:flex-row-reverse' %} gap-10 lg:gap-16 items-center">
            
            <div class="absolute top-6 {% cycle 'right-10', 'left-10' %} text-[8rem] font-black text-slate-50 opacity-50 pointer-events-none select-none z-0 tracking-tighter">
                0{{ forloop.index }}
            </div>

            <div class="absolute -bottom-10 {% cycle '-right-10', '-left-10' %} text-[15rem] opacity-5 group-hover:opacity-10 group-hover:scale-110 transition-all duration-700 pointer-events-none select-none z-0">
                {{ area.icon }}
            </div>

            <div class="flex-1 relative z-10 w-full">
                <div class="w-16 h-16 bg-gradient-to-br from-blue-50 to-cyan-50 text-blue-600 rounded-2xl flex items-center justify-center text-4xl mb-8 group-hover:scale-110 group-hover:shadow-lg group-hover:shadow-blue-100 transition-all duration-500 border border-blue-100/50">
                    {{ area.icon }}
                </div>
                <h2 class="text-3xl md:text-4xl font-bold text-slate-900 mb-6 tracking-tight">
                    {{ area.title }}
                </h2>
                <p class="text-lg text-slate-600 leading-relaxed mb-8">
                    {{ area.description }}
                </p>
                
                {% if area.image %}
                <div class="mt-8 rounded-3xl overflow-hidden shadow-lg border border-slate-100 relative group/img">
                    <div class="absolute inset-0 bg-blue-900/0 group-hover/img:bg-blue-900/10 transition-colors duration-500 z-10"></div>
                    <img src="{{ site.baseurl }}{{ area.image }}" alt="{{ area.title }}" class="w-full h-64 md:h-80 object-cover transform group-hover/img:scale-105 transition-transform duration-700">
                </div>
                {% endif %}
            </div>

            <div class="w-full md:w-5/12 relative z-10 flex flex-col justify-center">
                <div class="bg-slate-50/80 backdrop-blur-sm rounded-[2rem] p-8 md:p-10 border border-slate-100 group-hover:bg-blue-50/40 group-hover:border-blue-100 transition-colors duration-500 shadow-sm">
                    <h3 class="text-xs font-black text-blue-600 uppercase tracking-widest mb-6 flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-blue-500"></span> Key Focus Areas
                    </h3>
                    <ul class="space-y-6">
                        {% for point in area.points %}
                        <li class="group/item flex items-start text-slate-700 hover:text-blue-700 transition-colors">
                            <span class="flex-shrink-0 w-7 h-7 rounded-full bg-white border border-slate-200 text-blue-500 flex items-center justify-center mt-0.5 mr-4 group-hover/item:bg-blue-600 group-hover/item:text-white group-hover/item:border-blue-600 group-hover/item:scale-110 transition-all duration-300 shadow-sm">
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

<section class="bg-slate-900 py-24 mt-10 relative overflow-hidden">
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[40rem] h-[40rem] bg-blue-600 rounded-full blur-[100px] opacity-20 pointer-events-none"></div>
    
    <div class="max-w-4xl mx-auto px-4 text-center relative z-10">
        <h2 class="text-3xl md:text-4xl font-bold text-white mb-6">了解我们在这些领域的最新成果</h2>
        <p class="text-slate-400 mb-10 text-lg max-w-2xl mx-auto">我们的研究成果常年发表于 CVPR, ICCV, ECCV, NeurIPS 等国际顶级会议与期刊。代码与预训练模型均同步开源于社区。</p>
        
        <a href="{{ site.baseurl }}/pages/publications.html" class="inline-block bg-blue-600 text-white px-10 py-4 rounded-2xl font-bold hover:bg-blue-500 transition-all shadow-lg shadow-blue-900/50 hover:-translate-y-1 hover:shadow-xl hover:shadow-blue-900">
            查看学术成果 (Publications) &rarr;
        </a>
    </div>
</section>