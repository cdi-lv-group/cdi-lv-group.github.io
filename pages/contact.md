---
layout: default
title: 联系加入
---

<section class="bg-white border-b border-slate-100 py-16 md:py-24 relative overflow-hidden z-0">
    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMGg0MHY0MEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGQ9Ik0wIDM5LjVMMDQwIDM5LjUiIHN0cm9rZT0icmdiYSgwLCAwLCAwLCAwLjAzKSIgc3Ryb2tlLXdpZHRoPSIxIi8+PHBhdGggZD0iTTM5LjUgMEwzOS41IDQwIiBzdHJva2U9InJnYmEoMCwgMCwgMCwgMC4wMykiIHN0cm9rZS13aWR0aD0iMSIvPjwvc3ZnPg==')] opacity-40 -z-10"></div>
    <div class="absolute top-0 right-0 w-[30rem] h-[30rem] bg-blue-50 rounded-full blur-3xl opacity-60 -translate-y-1/2 translate-x-1/3 -z-10"></div>
    
    <div class="max-w-6xl mx-auto px-4 relative z-10 text-center md:text-left">
        <div class="inline-block mb-4 px-4 py-1.5 rounded-full bg-blue-50 border border-blue-100 text-blue-600 text-sm font-bold tracking-wide shadow-sm">
            Join {{ site.lab.group_short_name }}
        </div>
        <h1 class="text-4xl md:text-6xl font-extrabold text-slate-900 mb-6 tracking-tight leading-tight">
            与我们一起探索 <br class="hidden md:block" />
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500">智能的物理边界</span>
        </h1>
        <p class="text-lg md:text-xl text-slate-500 max-w-3xl leading-relaxed font-light mx-auto md:mx-0">
            我们常年招收对 3D 视觉、多模态感知与具身智能充满热忱的优秀博士生、硕士生及科研实习生。如果你热爱硬核技术并渴望在顶级学术舞台发声，欢迎加入！
        </p>
    </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-16 md:py-24">
    <div class="flex items-center space-x-4 mb-12 border-l-4 border-blue-600 pl-4">
        <h2 class="text-3xl font-bold text-slate-800 tracking-tight">开放职位</h2>
        <span class="text-slate-400 font-light italic">Open Positions</span>
    </div>

    <div class="grid md:grid-cols-3 gap-8">
        {% for position in site.data.positions %}
        {% assign border_color = "border-t-slate-500" %}
        {% assign icon_bg = "bg-slate-50" %}
        {% assign icon_text = "text-slate-600" %}
        
        {% if position.theme == "blue" %}
            {% assign border_color = "border-t-blue-500" %}
            {% assign icon_bg = "bg-blue-50" %}
            {% assign icon_text = "text-blue-600" %}
        {% elsif position.theme == "cyan" %}
            {% assign border_color = "border-t-cyan-500" %}
            {% assign icon_bg = "bg-cyan-50" %}
            {% assign icon_text = "text-cyan-600" %}
        {% elsif position.theme == "green" %}
            {% assign border_color = "border-t-green-500" %}
            {% assign icon_bg = "bg-green-50" %}
            {% assign icon_text = "text-green-600" %}
        {% endif %}

        <div class="bg-white rounded-[2rem] p-8 border border-slate-100 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col h-full border-t-4 {{ border_color }}">
            
            <div class="flex justify-between items-start mb-5">
                <div class="w-12 h-12 {{ icon_bg }} {{ icon_text }} rounded-xl flex items-center justify-center text-2xl shadow-sm">
                    {{ position.icon }}
                </div>
                {% if position.count %}
                <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold {{ icon_bg }} {{ icon_text }} border border-white shadow-sm mt-1">
                    名额: {{ position.count }}
                </span>
                {% endif %}
            </div>

            <h3 class="text-2xl font-bold text-slate-900 mb-2">{{ position.title }}</h3>
            
            {% if position.department %}
            <div class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-lg text-xs font-semibold text-slate-600 mb-4 w-fit">
                <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1v1H9V7zm5 0h1v1h-1V7zm-5 4h1v1H9v-1zm5 0h1v1h-1v-1zm-5 4h1v1H9v-1zm5 0h1v1h-1v-1z"></path></svg>
                招生依托：{{ position.department }}
            </div>
            {% endif %}

            <p class="text-slate-500 text-sm leading-relaxed mb-6 flex-grow">
                {{ position.description }}
            </p>
            
            <ul class="space-y-3 mt-auto pt-5 border-t border-slate-50 text-sm text-slate-600 font-medium">
                {% for tag in position.tags %}
                <li class="flex items-center gap-2">
                    <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg> 
                    {{ tag }}
                </li>
                {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </div>
</section>

<section class="bg-slate-50 py-20 border-y border-slate-100">
    <div class="max-w-6xl mx-auto px-4">
        <div class="text-center mb-16">
            <h2 class="text-3xl font-bold text-slate-800 tracking-tight mb-4">为什么选择我们？</h2>
            <p class="text-slate-500 max-w-2xl mx-auto">我们致力于为每一位实验室成员提供最顶尖的科研环境与最纯粹的学术氛围。</p>
        </div>
        
        <div class="grid md:grid-cols-3 gap-10">
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto bg-white rounded-full flex items-center justify-center shadow-sm mb-6 group-hover:-translate-y-2 transition-transform duration-300 border border-slate-100">
                    <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-slate-900 mb-3">充足的算力保障</h3>
                <p class="text-slate-500 text-sm leading-relaxed">配备大规模高性能 GPU 计算集群，告别算力焦虑，让你专注于核心算法创新与模型快速迭代。</p>
            </div>
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto bg-white rounded-full flex items-center justify-center shadow-sm mb-6 group-hover:-translate-y-2 transition-transform duration-300 border border-slate-100">
                    <svg class="w-8 h-8 text-cyan-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-slate-900 mb-3">一对一学术指导</h3>
                <p class="text-slate-500 text-sm leading-relaxed">导师亲自指导，从 Idea 构思、代码实现到论文撰写，提供全周期、高密度的科研训练与方向把控。</p>
            </div>
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto bg-white rounded-full flex items-center justify-center shadow-sm mb-6 group-hover:-translate-y-2 transition-transform duration-300 border border-slate-100">
                    <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-slate-900 mb-3">开放的国际视野</h3>
                <p class="text-slate-500 text-sm leading-relaxed">提供参与国际顶级学术会议（CVPR/NeurIPS等）交流的资助，并与海内外顶尖高校保持紧密合作。</p>
            </div>
        </div>
    </div>
</section>

<section class="max-w-4xl mx-auto px-4 py-20">
    <div class="bg-blue-600 rounded-[3rem] p-10 md:p-14 text-white shadow-2xl relative overflow-hidden text-center md:text-left">
        <div class="absolute top-0 right-0 w-64 h-64 bg-blue-500 rounded-full blur-3xl opacity-50 -mr-20 -mt-20 pointer-events-none"></div>
        <div class="absolute bottom-0 left-0 w-48 h-48 bg-blue-700 rounded-full blur-2xl opacity-50 -ml-10 -mb-10 pointer-events-none"></div>
        
        <div class="relative z-10 flex flex-col md:flex-row items-center gap-10">
            <div class="flex-1">
                <h2 class="text-3xl font-bold mb-4">如何申请？</h2>
                <p class="text-blue-100 mb-6 leading-relaxed">
                    请将您的个人简历（含专业排名、发表论文、项目经历）以及本科/硕士成绩单发送至下方邮箱。
                </p>
                <div class="bg-blue-800/40 border border-blue-400/30 rounded-2xl p-5 mb-8 text-sm text-blue-50 text-left">
                    <p class="font-bold text-white mb-2">📌 邮件主题格式建议：</p>
                    <code class="block bg-blue-900/50 p-3 rounded-lg text-blue-200 break-all">
                        [申请博士/硕士/实习] - 姓名 - 本科学校 - 预计入学年份
                    </code>
                </div>
                <a href="mailto:{{ site.lab.email }}" class="inline-flex items-center justify-center gap-2 bg-white text-blue-600 px-8 py-4 rounded-full font-bold text-lg hover:bg-blue-50 transition-all shadow-lg hover:-translate-y-1 w-full md:w-auto">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                    立即发送邮件
                </a>
            </div>
            
            <div class="hidden md:block flex-shrink-0">
                <div class="w-32 h-32 bg-blue-500/30 rounded-full flex items-center justify-center backdrop-blur-sm border border-blue-400/50">
                    <span class="text-5xl">✉️</span>
                </div>
            </div>
        </div>
    </div>
</section>