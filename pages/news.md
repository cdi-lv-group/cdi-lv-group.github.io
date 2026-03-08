---
layout: default
title: 新闻动态
---
<section class="bg-white dark:bg-slate-900 border-b border-slate-100 dark:border-slate-800 py-16 md:py-24 relative overflow-hidden z-0 transition-colors duration-300">
    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMGg0MHY0MEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGQ9Ik0wIDM5LjVMMDQwIDM5LjUiIHN0cm9rZT0icmdiYSgwLCAwLCAwLCAwLjAzKSIgc3Ryb2tlLXdpZHRoPSIxIi8+PHBhdGggZD0iTTM5LjUgMEwzOS41IDQwIiBzdHJva2U9InJnYmEoMCwgMCwgMCwgMC4wMykiIHN0cm9rZS13aWR0aD0iMSIvPjwvc3ZnPg==')] opacity-60 dark:opacity-10 dark:invert transition-all duration-300 -z-10"></div>
    <div class="absolute top-0 right-0 w-[40rem] h-[40rem] bg-cyan-50 dark:bg-cyan-900/20 rounded-full blur-3xl opacity-60 -translate-y-1/2 translate-x-1/3 transition-colors duration-300 -z-10"></div>
    <div class="absolute bottom-0 left-0 w-[30rem] h-[30rem] bg-blue-50 dark:bg-blue-900/20 rounded-full blur-3xl opacity-40 translate-y-1/3 -translate-x-1/3 transition-colors duration-300 -z-10"></div>
    
    <div class="max-w-6xl mx-auto px-4 relative z-10 text-center md:text-left">
        <div class="inline-block mb-4 px-4 py-1.5 rounded-full bg-blue-50 dark:bg-slate-800 border border-blue-100 dark:border-blue-900 text-blue-600 dark:text-blue-400 text-sm font-bold tracking-wide shadow-sm transition-colors duration-300">
            <span class="lang-zh">新闻动态</span>
            <span class="lang-en">Latest News</span>
        </div>
        <h1 class="text-4xl md:text-6xl font-extrabold text-slate-900 dark:text-white mb-6 tracking-tight leading-tight transition-colors duration-300">
            <span class="lang-zh">记录实验室的 <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">重要时刻</span></span>
            <span class="lang-en">Capturing Our <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">Milestones</span></span>
        </h1>
        <p class="text-lg md:text-xl text-slate-500 dark:text-slate-400 max-w-3xl leading-relaxed font-light mx-auto md:mx-0 transition-colors duration-300">
            <span class="lang-zh">记录 LV 课题组在学术研究、开源项目、团队建设与产业合作上的每一个重要里程碑。</span>
            <span class="lang-en">Highlighting LV Lab's significant progress in academic research, open-source projects, team building, and industrial collaborations.</span>
        </p>
    </div>
</section>

<section class="max-w-5xl mx-auto px-4 py-16 md:py-24">
    <div class="relative">
        <div class="absolute left-4 md:left-1/2 top-0 bottom-0 w-0.5 bg-slate-200 dark:bg-slate-800 -translate-x-1/2 hidden md:block transition-colors duration-300"></div>

        <div class="space-y-16">
            {% for item in site.data.news %}
            <div class="relative flex flex-col md:flex-row items-center group {% cycle '', 'md:flex-row-reverse' %}">
                
                <div class="absolute left-4 md:left-1/2 w-4 h-4 bg-white dark:bg-slate-900 border-4 border-blue-500 dark:border-blue-400 rounded-full -translate-x-1/2 z-10 group-hover:scale-150 group-hover:bg-blue-600 transition-all duration-300"></div>
                
                <div class="w-full md:w-1/2 mb-2 md:mb-0 px-12 md:px-16 text-left {% cycle 'md:text-right', 'md:text-left' %}">
                    <span class="text-lg font-black text-slate-400 dark:text-slate-600 tracking-tighter transition-colors">
                        {{ item.date }}
                    </span>
                </div>

                <div class="w-full md:w-1/2 px-4 md:px-10">
                    <div class="bg-white dark:bg-slate-800 rounded-[2.5rem] p-6 md:p-8 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-2xl hover:-translate-y-1 transition-all duration-500 relative overflow-hidden">
                        
                        <div class="mb-4">
                            <span class="inline-block px-3 py-1 rounded-lg bg-blue-50 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400 text-[10px] font-black uppercase tracking-widest border border-blue-100 dark:border-blue-800 transition-colors">
                                <span class="lang-zh">{{ item.category.zh }}</span>
                                <span class="lang-en">{{ item.category.en }}</span>
                            </span>
                        </div>

                        <h3 class="text-xl md:text-2xl font-bold text-slate-900 dark:text-white mb-4 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors leading-tight">
                            <span class="lang-zh">{{ item.title.zh }}</span>
                            <span class="lang-en">{{ item.title.en }}</span>
                        </h3>

                        <p class="text-slate-600 dark:text-slate-400 text-sm md:text-base leading-relaxed mb-6 font-light transition-colors">
                            <span class="lang-zh">{{ item.description.zh }}</span>
                            <span class="lang-en">{{ item.description.en }}</span>
                        </p>

                        {% if item.link and item.link != "#" %}
                        <div class="pt-4 border-t border-slate-50 dark:border-slate-700/50">
                            <a href="{{ item.link }}" target="_blank" class="inline-flex items-center text-sm font-bold text-blue-600 dark:text-blue-400 group/link">
                                <span class="lang-zh">了解更多</span>
                                <span class="lang-en">Learn More</span>
                                <svg class="w-4 h-4 ml-1 transform group-hover/link:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6"></path></svg>
                            </a>
                        </div>
                        {% endif %}
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>

<section class="max-w-4xl mx-auto px-4 pb-24">
    <div class="bg-gradient-to-br from-blue-600 to-cyan-600 rounded-[3rem] p-8 md:p-12 text-center text-white shadow-xl shadow-blue-200 dark:shadow-none transition-all">
        <h2 class="text-2xl md:text-3xl font-bold mb-4">
            <span class="lang-zh">想了解实验室的最新开源动态？</span>
            <span class="lang-en">Stay Updated with Our Open Source</span>
        </h2>
        <p class="text-blue-50 opacity-90 mb-8 max-w-xl mx-auto font-light leading-relaxed">
            <span class="lang-zh">关注我们课题组的官方 GitHub 组织，获取最新发布的论文代码与预训练模型。</span>
            <span class="lang-en">Follow our official GitHub organization to access the latest paper codes and pre-trained models.</span>
        </p>
        <a href="{{ site.lab.github }}" target="_blank" class="inline-flex items-center gap-2 bg-white text-blue-600 px-8 py-4 rounded-2xl font-black hover:bg-blue-50 transition transform hover:-translate-y-1 shadow-lg">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" /></svg>
            <span class="lang-zh">前往 GitHub 主页</span>
            <span class="lang-en">Go to GitHub</span>
        </a>
    </div>
</section>