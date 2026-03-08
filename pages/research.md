---
layout: default
title: 研究方向
---

<section class="bg-white border-b border-slate-100 py-16 md:py-20 relative overflow-hidden">
    <div class="absolute top-0 right-0 w-[30rem] h-[30rem] bg-cyan-50 rounded-full blur-3xl opacity-50 -translate-y-1/2 translate-x-1/3 -z-10"></div>
    
    <div class="max-w-6xl mx-auto px-4 relative z-10">
        <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 mb-6 tracking-tight">
            探索智能的物理边界
        </h1>
        <p class="text-lg md:text-xl text-slate-500 max-w-3xl leading-relaxed font-light">
            我们致力于多模态感知、3D视觉与具身智能的基础理论与前沿应用研究，旨在让智能体在复杂、不确定的真实世界中具备强大的自主行为能力。
        </p>
    </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-16 md:py-24">
    
    <div class="space-y-16">
        {% for area in site.data.research %}
        <div class="group bg-white rounded-[2.5rem] p-8 md:p-12 border border-slate-100 shadow-sm hover:shadow-2xl transition-all duration-500 relative overflow-hidden flex flex-col md:flex-row gap-10 lg:gap-16">
            
            <div class="absolute -bottom-10 -right-10 text-[15rem] opacity-5 group-hover:opacity-10 transition-opacity duration-500 pointer-events-none select-none">
                {{ area.icon }}
            </div>

            <div class="flex-1 relative z-10">
                <div class="w-16 h-16 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center text-4xl mb-8 group-hover:scale-110 transition-transform duration-500">
                    {{ area.icon }}
                </div>
                <h2 class="text-3xl md:text-4xl font-bold text-slate-900 mb-6 tracking-tight">
                    {{ area.title }}
                </h2>
                <p class="text-lg text-slate-600 leading-relaxed mb-8">
                    {{ area.description }}
                </p>
                
                {% if area.image %}
                <div class="mt-8 rounded-2xl overflow-hidden shadow-lg border border-slate-100">
                    <img src="{{ site.baseurl }}{{ area.image }}" alt="{{ area.title }}" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-700">
                </div>
                {% endif %}
            </div>

            <div class="md:w-5/12 relative z-10 flex flex-col justify-center">
                <div class="bg-slate-50 rounded-3xl p-8 border border-slate-100 group-hover:bg-blue-50/50 transition-colors duration-500">
                    <h3 class="text-sm font-bold text-slate-400 uppercase tracking-widest mb-6">Key Focus Areas</h3>
                    <ul class="space-y-5">
                        {% for point in area.points %}
                        <li class="flex items-start text-slate-700">
                            <span class="flex-shrink-0 w-6 h-6 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center mt-0.5 mr-4 group-hover:bg-blue-600 group-hover:text-white transition-colors duration-300">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
                            </span>
                            <span class="leading-relaxed font-medium">{{ point }}</span>
                        </li>
                        {% endfor %}
                    </ul>
                </div>
            </div>

        </div>
        {% endfor %}
    </div>

</section>

<section class="bg-slate-900 py-20 mt-10">
    <div class="max-w-4xl mx-auto px-4 text-center">
        <h2 class="text-3xl font-bold text-white mb-6">了解我们在这些领域的最新成果</h2>
        <p class="text-slate-400 mb-10 text-lg">我们的研究成果常年发表于 CVPR, ICCV, ECCV, NeurIPS 等顶级会议与期刊。</p>
        <a href="{{ site.baseurl }}/publications" class="inline-block bg-blue-600 text-white px-10 py-4 rounded-2xl font-bold hover:bg-blue-500 transition-all shadow-lg hover:-translate-y-1">
            查看学术成果 (Publications)
        </a>
    </div>
</section>