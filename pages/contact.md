---
layout: default
title: 联系加入
---

<section class="bg-white dark:bg-slate-900 border-b border-slate-100 dark:border-slate-800 py-16 md:py-24 relative overflow-hidden z-0 transition-colors duration-300">
    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMGg0MHY0MEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGQ9Ik0wIDM5LjVMMDQwIDM5LjUiIHN0cm9rZT0icmdiYSgwLCAwLCAwLCAwLjAzKSIgc3Ryb2tlLXdpZHRoPSIxIi8+PHBhdGggZD0iTTM5LjUgMEwzOS41IDQwIiBzdHJva2U9InJnYmEoMCwgMCwgMCwgMC4wMykiIHN0cm9rZS13aWR0aD0iMSIvPjwvc3ZnPg==')] dark:opacity-[0.05] dark:invert opacity-40 -z-10 transition-opacity"></div>
    <div class="absolute top-0 right-0 w-[40rem] h-[40rem] bg-cyan-50 dark:bg-cyan-900/20 rounded-full blur-3xl opacity-60 -translate-y-1/2 translate-x-1/3 transition-colors duration-300 -z-10"></div>
    
    <div class="max-w-6xl mx-auto px-4 relative z-10 text-center md:text-left">
        <div class="inline-block mb-4 px-4 py-1.5 rounded-full bg-blue-50 dark:bg-slate-800 border border-blue-100 dark:border-blue-900 text-blue-600 dark:text-blue-400 text-sm font-bold tracking-wide shadow-sm transition-colors">
            <span class="lang-zh">加入 {{ site.lab.group_short_name }}</span>
            <span class="lang-en">Join {{ site.lab.group_short_name }}</span>
        </div>
        <h1 class="text-4xl md:text-6xl font-extrabold text-slate-900 dark:text-white mb-6 tracking-tight leading-tight transition-colors">
            <span class="lang-zh">与我们一起探索 <br class="hidden md:block" /> <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">智能的物理边界</span></span>
            <span class="lang-en">Exploring the <br class="hidden md:block" /> <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">Physical Boundaries</span> of AI</span>
        </h1>
        <p class="text-lg md:text-xl text-slate-500 dark:text-slate-400 max-w-3xl leading-relaxed font-light mx-auto md:mx-0 transition-colors">
            <span class="lang-zh">我们常年招收对 3D 视觉、多模态感知与具身智能充满热忱的优秀博士生、硕士生及科研实习生。如果你热爱硬核技术并渴望在顶级学术舞台发声，欢迎加入！</span>
            <span class="lang-en">We are constantly looking for talented Ph.D., Master students, and Research Interns passionate about 3D Vision, Multimodal Perception, and Embodied AI. If you love hardcore technology, join us!</span>
        </p>
    </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-16 md:py-24">
    <div class="flex items-center space-x-4 mb-12 border-l-4 border-blue-600 dark:border-blue-500 pl-4 transition-colors">
        <h2 class="text-3xl font-bold text-slate-800 dark:text-white tracking-tight transition-colors">
            <span class="lang-zh">开放职位</span>
            <span class="lang-en">Open Positions</span>
        </h2>
    </div>

    <div class="grid md:grid-cols-3 gap-8">
        {% for position in site.data.positions %}
        {% if position.theme == "blue" %}
            {% assign color_class = "blue" %}
        {% elsif position.theme == "cyan" %}
            {% assign color_class = "cyan" %}
        {% elsif position.theme == "green" %}
            {% assign color_class = "green" %}
        {% else %}
            {% assign color_class = "slate" %}
        {% endif %}

        <div class="bg-white dark:bg-slate-800 rounded-[2.5rem] p-8 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-2xl hover:-translate-y-2 transition-all duration-500 flex flex-col h-full border-t-4 border-t-{{ color_class }}-500">
            
            <div class="flex justify-between items-start mb-6">
                <div class="w-14 h-14 bg-{{ color_class }}-50 dark:bg-{{ color_class }}-900/30 text-{{ color_class }}-600 dark:text-{{ color_class }}-400 rounded-2xl flex items-center justify-center text-3xl shadow-sm transition-colors">
                    {{ position.icon }}
                </div>
                {% if position.count %}
                <span class="inline-flex items-center px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest bg-{{ color_class }}-50 dark:bg-{{ color_class }}-900/30 text-{{ color_class }}-600 dark:text-{{ color_class }}-400 border border-{{ color_class }}-100 dark:border-{{ color_class }}-800 transition-colors">
                    <span class="lang-zh">名额: {{ position.count.zh }}</span>
                    <span class="lang-en">{{ position.count.en }}</span>
                </span>
                {% endif %}
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-2 transition-colors">
                <span class="lang-zh">{{ position.title.zh }}</span>
                <span class="lang-en">{{ position.title.en }}</span>
            </h3>
            
            <div class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-slate-50 dark:bg-slate-700/50 border border-slate-100 dark:border-slate-600 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-300 mb-6 w-fit transition-colors">
                <svg class="w-3.5 h-3.5 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1v1H9V7zm5 0h1v1h-1V7zm-5 4h1v1H9v-1zm5 0h1v1h-1v-1zm-5 4h1v1H9v-1zm5 0h1v1h-1v-1z"></path></svg>
                <span class="lang-zh">招生依托：{{ position.department.zh }}</span>
                <span class="lang-en">Affiliation: {{ position.department.en }}</span>
            </div>

            <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed mb-8 flex-grow transition-colors font-light">
                <span class="lang-zh">{{ position.description.zh }}</span>
                <span class="lang-en">{{ position.description.en }}</span>
            </p>
            
            <div class="flex flex-wrap gap-2 mt-auto pt-6 border-t border-slate-50 dark:border-slate-700/50">
                <div class="lang-zh flex flex-wrap gap-2">
                    {% for tag in position.tags.zh %}
                    <span class="flex items-center gap-1.5 text-xs font-bold text-{{ color_class }}-600 dark:text-{{ color_class }}-400">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg> {{ tag }}
                    </span>
                    {% endfor %}
                </div>
                <div class="lang-en flex flex-wrap gap-2">
                    {% for tag in position.tags.en %}
                    <span class="flex items-center gap-1.5 text-xs font-bold text-{{ color_class }}-600 dark:text-{{ color_class }}-400">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg> {{ tag }}
                    </span>
                    {% endfor %}
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</section>

<section class="bg-slate-50 dark:bg-slate-800/50 py-20 border-y border-slate-100 dark:border-slate-800 transition-colors duration-300">
    <div class="max-w-6xl mx-auto px-4">
        <div class="text-center mb-16">
            <h2 class="text-3xl font-bold text-slate-800 dark:text-white tracking-tight mb-4 transition-colors">
                <span class="lang-zh">为什么选择我们？</span>
                <span class="lang-en">Why Join Us?</span>
            </h2>
        </div>
        
        <div class="grid md:grid-cols-3 gap-12">
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto bg-white dark:bg-slate-800 rounded-3xl flex items-center justify-center shadow-sm mb-6 group-hover:-translate-y-2 transition-all duration-300 border border-slate-100 dark:border-slate-700">
                    <svg class="w-10 h-10 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">
                    <span class="lang-zh">充足的算力保障</span>
                    <span class="lang-en">Abundant Computing Power</span>
                </h3>
                <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                    <span class="lang-zh">配备大规模高性能 GPU 计算集群，告别算力焦虑。</span>
                    <span class="lang-en">Equipped with large-scale high-performance GPU clusters.</span>
                </p>
            </div>
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto bg-white dark:bg-slate-800 rounded-3xl flex items-center justify-center shadow-sm mb-6 group-hover:-translate-y-2 transition-all duration-300 border border-slate-100 dark:border-slate-700">
                    <svg class="w-10 h-10 text-cyan-600 dark:text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">
                    <span class="lang-zh">一对一学术指导</span>
                    <span class="lang-en">Mentorship</span>
                </h3>
                <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                    <span class="lang-zh">导师亲自指导 Idea 构思与论文撰写。</span>
                    <span class="lang-en">Direct guidance from mentors on ideas and writing.</span>
                </p>
            </div>
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto bg-white dark:bg-slate-800 rounded-3xl flex items-center justify-center shadow-sm mb-6 group-hover:-translate-y-2 transition-all duration-300 border border-slate-100 dark:border-slate-700">
                    <svg class="w-10 h-10 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">
                    <span class="lang-zh">开放的国际视野</span>
                    <span class="lang-en">Global Vision</span>
                </h3>
                <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                    <span class="lang-zh">资助参与国际顶会交流（CVPR/NeurIPS等）。</span>
                    <span class="lang-en">Funding for international conferences like CVPR.</span>
                </p>
            </div>
        </div>
    </div>
</section>

<section class="max-w-4xl mx-auto px-4 py-20 mb-20">
    <div class="bg-gradient-to-br from-blue-600 to-indigo-700 rounded-[3.5rem] p-10 md:p-14 text-white shadow-2xl relative overflow-hidden transition-colors duration-300">
        <div class="absolute top-0 right-0 w-80 h-80 bg-white/10 rounded-full blur-3xl -mr-20 -mt-20"></div>
        
        <div class="relative z-10 flex flex-col md:flex-row items-center gap-12">
            <div class="flex-1 text-center md:text-left">
                <h2 class="text-4xl font-black mb-6">
                    <span class="lang-zh">如何申请？</span>
                    <span class="lang-en">How to Apply?</span>
                </h2>
                <p class="text-blue-50 opacity-90 mb-8 text-lg font-light leading-relaxed">
                    <span class="lang-zh">请将个人简历及成绩单发送至下方邮箱。</span>
                    <span class="lang-en">Please send your CV and transcripts to the following email.</span>
                </p>
                
                <div class="bg-black/20 backdrop-blur-md border border-white/10 rounded-2xl p-6 mb-10 text-left">
                    <p class="font-bold text-white mb-3 flex items-center gap-2">
                        <span class="lang-zh">📌 邮件主题格式建议：</span>
                        <span class="lang-en">📌 Subject Format:</span>
                    </p>
                    <code class="block bg-white/10 p-4 rounded-xl text-blue-100 text-sm break-all font-mono">
                        <span class="lang-zh">[申请博士/硕士/实习] - 姓名 - 本科学校 - 入学年份</span>
                        <span class="lang-en">[Apply-PhD/Master/Intern] - Name - Univ - Year</span>
                    </code>
                </div>
                
                <a href="mailto:{{ site.lab.email }}" class="inline-flex items-center justify-center gap-3 bg-white text-blue-600 px-10 py-5 rounded-2xl font-black text-xl hover:scale-105 transition shadow-xl w-full md:w-auto">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                    <span class="lang-zh">立即发送邮件</span>
                    <span class="lang-en">Email Us Now</span>
                </a>
            </div>
            
            <div class="hidden lg:block w-48 h-48 bg-white/10 rounded-full flex items-center justify-center border border-white/20">
                <span class="text-7xl animate-bounce">✉️</span>
            </div>
        </div>
    </div>
</section>