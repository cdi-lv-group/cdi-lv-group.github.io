---
layout: default
title: 新闻动态
---

<section class="bg-white border-b border-slate-100 py-16 md:py-20 relative overflow-hidden">
    <div class="absolute top-0 right-0 w-[30rem] h-[30rem] bg-blue-50 rounded-full blur-3xl opacity-50 -translate-y-1/2 translate-x-1/3 -z-10"></div>
    
    <div class="max-w-4xl mx-auto px-4 relative z-10 text-center">
        <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 mb-6 tracking-tight">新闻动态</h1>
        <p class="text-lg md:text-xl text-slate-500 leading-relaxed font-light">
            记录 LV 课题组在学术研究、开源项目、团队建设与产业合作上的每一个重要里程碑。
        </p>
    </div>
</section>

<section class="max-w-4xl mx-auto px-4 py-16 md:py-24">
    
    <div class="relative">
        <div class="absolute left-4 md:left-8 top-0 bottom-0 w-0.5 bg-slate-200"></div>

        <div class="space-y-12">
            {% for item in site.data.news %}
            <div class="relative pl-12 md:pl-20 group">
                
                <div class="absolute left-[0.6rem] md:left-[1.65rem] top-1.5 w-4 h-4 bg-white border-4 border-blue-500 rounded-full group-hover:bg-blue-600 group-hover:scale-125 transition-all duration-300 shadow-sm z-10"></div>
                
                <div class="bg-white rounded-[2rem] p-6 md:p-8 border border-slate-100 shadow-sm hover:shadow-xl transition-all duration-500 transform group-hover:-translate-y-1">
                    
                    <div class="flex flex-wrap items-center justify-between gap-4 mb-4">
                        <span class="text-sm font-black text-blue-600 tracking-wider">
                            {{ item.date }}
                        </span>
                        {% if item.category %}
                        <span class="inline-block px-3 py-1 bg-slate-50 text-slate-500 text-xs font-bold rounded-md tracking-wide uppercase border border-slate-100">
                            {{ item.category }}
                        </span>
                        {% endif %}
                    </div>
                    
                    <h3 class="text-xl md:text-2xl font-bold text-slate-900 mb-4 group-hover:text-blue-600 transition-colors leading-snug">
                        {{ item.title }}
                    </h3>
                    
                    <p class="text-slate-600 leading-relaxed mb-6 text-sm md:text-base">
                        {{ item.description }}
                    </p>
                    
                    {% if item.link %}
                    <div class="mt-auto pt-4 border-t border-slate-50">
                        <a href="{{ item.link }}" target="_blank" class="inline-flex items-center text-sm font-semibold text-blue-600 hover:text-blue-800 transition">
                            了解详情 
                            <svg class="w-4 h-4 ml-1 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                        </a>
                    </div>
                    {% endif %}
                </div>
            </div>
            {% endfor %}
            
            <div class="relative pl-12 md:pl-20 pt-4">
                <div class="absolute left-[0.6rem] md:left-[1.65rem] top-6 w-4 h-4 bg-slate-200 rounded-full"></div>
                <p class="text-sm font-medium text-slate-400 italic">实验室故事从此开始...</p>
            </div>
        </div>
    </div>

</section>

<section class="bg-blue-50 py-16 mb-20 rounded-[3rem] max-w-4xl mx-auto px-4 text-center border border-blue-100">
    <h2 class="text-2xl font-bold text-slate-800 mb-4">想了解实验室的最新开源动态？</h2>
    <p class="text-slate-600 mb-8 max-w-xl mx-auto">关注我们课题组的官方 GitHub 组织，获取最新发布的论文代码与预训练模型，加入我们的开源生态。</p>
    <a href="{{ site.lab.github }}" target="_blank" class="inline-flex items-center gap-2 bg-blue-600 text-white px-8 py-3 rounded-xl font-bold hover:bg-blue-700 transition shadow-lg shadow-blue-200">
        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"></path></svg>
        前往 GitHub 主页
    </a>
</section>