from config import ASSISTANT_NAME
from helpers.bot_utils import BOT_NAME, USERNAME


START_TEXT = f"👋🏻 **مرحبا**, \n\n هذا هو **{BOT_NAME}** \nيمكنني البث المباشر والراديو ومقاطع الفيديو على يوتيوب  وملفات الصوت / الفيديو تليجرام على الدردشة الصوتية لمجموعات تليجرام . لنستمتع بمنظر سينمائي لمشغل الفيديو الجماعي مع أصدقائك 😉! \n\n**مصنوع من ❤️ بواسطة الباشمبرج سيمبا** 👑"
HELP_TEXT = f"""
🛠-- **إعداد البوت**:--

\u2022 ابدأ الدردشة الصوتية في مجموعتك!
\u2022 أضفني (@{USERNAME}) & مساعدي (@{ASSISTANT_NAME}) إلى مجموعتك!
\u2022 أعط المسؤول لي (@{USERNAME}) & مساعدي (@{ASSISTANT_NAME}) في مجموعتك!

⚔️-- **الأوامر المتوفرة**:--

\u2022 `/play` - Stream An Audio
\u2022 `/stream` - Stream An Video
\u2022 `/pause` - Pause Current Stream
\u2022 `/resume` - Resume Paused Stream
\u2022 `/endstream` - End Stream & Left VC
\u2022 `/restart` - Restart Bot (Sudo Only)
"""
ABOUT_TEXT = f"💡-- **معلومة**:-- \n\nتم إنشاء هذا الروبوت لدفق مقاطع الفيديو في دردشات الفيديو الجماعية برقية باستخدام عدة طرق من WebRTC. مدعوم من pytgcalls ، واجهة برمجة تطبيقات العميل غير المتزامن لـ Telegram Group Calls و Pyrogram ، مكتبة وإطار عمل Telegram MTProto API في Pure Python للمستخدمين والروبوتات.\n\n**هذا الروبوت مرخص بموجب ترخيص GNU-GPL 3.0!**"
