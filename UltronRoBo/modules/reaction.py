"""
MIT License

Copyright (c) 2021 UltronRoBo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import random

from UltronRoBo import dispatcher
from UltronRoBo.modules.disable import DisableAbleCommandHandler
from telegram import Update
from telegram.ext import CallbackContext, run_async

reactions = [
    "( ͡° ͜ʖ ͡°)", "( . •́ _ʖ •̀ .)", "( ಠ ͜ʖ ಠ)", "( ͡ ͜ʖ ͡ )", "(ʘ ͜ʖ ʘ)",
    "ヾ(´〇`)ﾉ♪♪♪", "ヽ(o´∀`)ﾉ♪♬", "♪♬((d⌒ω⌒b))♬♪", "└(＾＾)┐", "(￣▽￣)/♫•*¨*•.¸¸♪",
    "ヾ(⌐■_■)ノ♪", "乁( • ω •乁)", "♬♫♪◖(● o ●)◗♪♫♬", "(っ˘ڡ˘ς)", "( ˘▽˘)っ♨",
    "(　・ω・)⊃-[二二]", "(*´ー`)旦 旦(￣ω￣*)", "( ￣▽￣)[] [](≧▽≦ )", "(*￣▽￣)旦 且(´∀`*)",
    "(ノ ˘_˘)ノ　ζ|||ζ　ζ|||ζ　ζ|||ζ", "(ノ°∀°)ノ⌒･*:.｡. .｡.:*･゜ﾟ･*☆",
    "(⊃｡•́‿•̀｡)⊃━✿✿✿✿✿✿", "(∩` ﾛ ´)⊃━炎炎炎炎炎", "( ・∀・)・・・--------☆",
    "( -ω-)／占~~~~~", "○∞∞∞∞ヽ(^ー^ )", "(*＾＾)/~~~~~~~~~~◎", "((( ￣□)_／",
    "(ﾒ￣▽￣)︻┳═一", "ヽ( ･∀･)ﾉ_θ彡☆Σ(ノ `Д´)ノ", "(*`0´)θ☆(メ°皿°)ﾉ",
    "(; -_-)――――――C<―_-)", "ヽ(>_<ヽ) ―⊂|=0ヘ(^‿^ )", "(҂` ﾛ ´)︻デ═一 ＼(º □ º l|l)/",
    "/( .□.)＼ ︵╰(°益°)╯︵ /(.□. /)", "(`⌒*)O-(`⌒´Q)", "(っ•﹏•)っ ✴==≡눈٩(`皿´҂)ง",
    "ヾ(・ω・)メ(・ω・)ノ", "(*^ω^)八(⌒▽⌒)八(-‿‿- )ヽ", "ヽ( ⌒ω⌒)人(=^‥^= )ﾉ",
    "｡*:☆(・ω・人・ω・)｡:゜☆｡", "(°(°ω(°ω°(☆ω☆)°ω°)ω°)°)", "(っ˘▽˘)(˘▽˘)˘▽˘ς)",
    "(*＾ω＾)人(＾ω＾*)", "＼(▽￣ \ (￣▽￣) / ￣▽)／", "(￣Θ￣)", "＼( ˋ Θ ´ )／",
    "( ´(00)ˋ )", "＼(￣(oo)￣)／", "／(≧ x ≦)＼", "／(=･ x ･=)＼", "(=^･ω･^=)",
    "(= ; ｪ ; =)", "(=⌒‿‿⌒=)", "(＾• ω •＾)", "ଲ(ⓛ ω ⓛ)ଲ", "ଲ(ⓛ ω ⓛ)ଲ", "(^◔ᴥ◔^)",
    "[(－－)]..zzZ", "(￣o￣) zzZZzzZZ", "(＿ ＿*) Z z z", "☆ﾐ(o*･ω･)ﾉ",
    "ε=ε=ε=ε=┌(;￣▽￣)┘", "ε===(っ≧ω≦)っ", "__φ(．．)", "ヾ( `ー´)シφ__", "( ^▽^)ψ__",
    "|･ω･)", "|д･)", "┬┴┬┴┤･ω･)ﾉ", "|･д･)ﾉ", "(*￣ii￣)", "(＾〃＾)", "m(_ _)m",
    "人(_ _*)", "(シ. .)シ", "(^_~)", "(>ω^)", "(^_<)〜☆", "(^_<)", "(づ￣ ³￣)づ",
    "(⊃｡•́‿•̀｡)⊃", "⊂(´• ω •`⊂)", "(*・ω・)ﾉ", "(^-^*)/", "ヾ(*'▽'*)", "(^０^)ノ",
    "(*°ｰ°)ﾉ", "(￣ω￣)/", "(≧▽≦)/", "w(°ｏ°)w", "(⊙_⊙)", "(°ロ°) !", "∑(O_O;)",
    "(￢_￢)", "(¬_¬ )", "(↼_↼)", "(￣ω￣;)", "┐('～`;)┌", "(・_・;)", "(＠_＠)",
    "(•ิ_•ิ)?", "ヽ(ー_ー )ノ", "┐(￣ヘ￣)┌", "┐(￣～￣)┌", "┐( ´ д ` )┌", "╮(︶▽︶)╭",
    "ᕕ( ᐛ )ᕗ", "(ノωヽ)", "(″ロ゛)", "(/ω＼)", "(((＞＜)))", "~(>_<~)", "(×_×)",
    "(×﹏×)", "(ノ_<。)", "(μ_μ)", "o(TヘTo)", "( ﾟ，_ゝ｀)", "( ╥ω╥ )", "(／ˍ・、)",
    "(つω`｡)", "(T_T)", "o(〒﹏〒)o", "(＃`Д´)", "(・`ω´・)", "( `ε´ )", "(ﾒ` ﾛ ´)",
    "Σ(▼□▼メ)", "(҂ `з´ )", "٩(╬ʘ益ʘ╬)۶", "↑_(ΦwΦ)Ψ", "(ﾉಥ益ಥ)ﾉ", "(＃＞＜)",
    "(；￣Д￣)", "(￢_￢;)", "(＾＾＃)", "(￣︿￣)", "ヾ( ￣O￣)ツ", "(ᗒᗣᗕ)՞",
    "(ノ_<。)ヾ(´ ▽ ` )", "ヽ(￣ω￣(。。 )ゝ", "(ﾉ_；)ヾ(´ ∀ ` )", "(´-ω-`( _ _ )",
    "(⌒_⌒;)", "(*/_＼)", "( ◡‿◡ *)", "(//ω//)", "(￣▽￣*)ゞ", "(„ಡωಡ„)",
    "(ﾉ´ з `)ノ", "(♡-_-♡)", "(─‿‿─)♡", "(´ ω `♡)", "(ღ˘⌣˘ღ)", "(´• ω •`) ♡",
    "╰(*´︶`*)╯♡", "(≧◡≦) ♡", "♡ (˘▽˘>ԅ( ˘⌣˘)", "σ(≧ε≦σ) ♡", "(˘∀˘)/(μ‿μ) ❤",
    "Σ>―(〃°ω°〃)♡→", "(* ^ ω ^)", "(o^▽^o)", "ヽ(・∀・)ﾉ", "(o･ω･o)", "(^人^)",
    "( ´ ω ` )", "(´• ω •`)", "╰(▔∀▔)╯", "(✯◡✯)", "(⌒‿⌒)", "(*°▽°*)",
    "(´｡• ᵕ •｡`)", "ヽ(>∀<☆)ノ", "＼(￣▽￣)／", "(o˘◡˘o)", "(╯✧▽✧)╯", "( ‾́ ◡ ‾́ )",
    "(๑˘︶˘๑)", "(´･ᴗ･ ` )", "( ͡° ʖ̯ ͡°)", "( ఠ ͟ʖ ఠ)", "( ಥ ʖ̯ ಥ)", "(≖ ͜ʖ≖)",
    "ヘ(￣ω￣ヘ)", "(ﾉ≧∀≦)ﾉ", "└(￣-￣└))", "┌(＾＾)┘", "(^_^♪)", "(〜￣△￣)〜",
    "(｢• ω •)｢", "( ˘ ɜ˘) ♬♪♫", "( o˘◡˘o) ┌iii┐", "♨o(>_<)o♨",
    "( ・・)つ―{}@{}@{}-", "(*´з`)口ﾟ｡ﾟ口(・∀・ )", "( *^^)o∀*∀o(^^* )", "-●●●-ｃ(・・ )",
    "(ﾉ≧∀≦)ﾉ ‥…━━━★", "╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ", "(∩ᄑ_ᄑ)⊃━☆ﾟ*･｡*･:≡( ε:)"
]


@run_async
def react(update: Update, context: CallbackContext):
    message = update.effective_message
    react = random.choice(reactions)
    if message.reply_to_message:
        message.reply_to_message.reply_text(react)
    else:
        message.reply_text(react)


REACT_HANDLER = DisableAbleCommandHandler("react", react)

dispatcher.add_handler(REACT_HANDLER)

__mod_name__ = "Reactions"
__command_list__ = ["react"]
__handlers__ = [REACT_HANDLER]
