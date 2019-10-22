window.AudioContext = window.AudioContext || window.webkitAudioContext
window.琴 =
    容器: new AudioContext()
    碎月: [
            3, 5, 6, 8, 9, '', 8, 9, 10,'', 8, 6, 5, 3, 8, 9, 6,'',
            6, 8, 9, '', 8, 9, 10, '', 12, 13, 15, 14, 13, 12, 13,'',
            12, 10, 9, '', 10, 8, 9, '', 8, 9, 10, 6, 9, 8, 6,'',
            6, 5, 6, '', 8, 9, 9, 8, 5, 6, ''
        ]

    p: 0
    叮: ->
        鍵 = this.碎月[this.p]
        this.p += 1
        if this.p == this.碎月.length
            this.p = 0
        if 鍵 == ''
            this.叮()
            return
        this.彈鍵(鍵, 0.3)

    取頻率: (x, c1 = 440) ->
        對應 = [0, 2, 4, 5, 7, 9, 11]
        a = (x - 1) % 7
        b = Math.floor((x - 1) / 7)
        return c1 * Math.pow(2, 1 / 12 * 對應[a] + b)

    播音: (頻率, 音量) ->
        oscillator = this.容器.createOscillator()
        gainNode = this.容器.createGain()
        oscillator.connect(gainNode)
        gainNode.connect(this.容器.destination)
        oscillator.frequency.value = 頻率
        gainNode.gain.setValueAtTime(0, this.容器.currentTime)
        gainNode.gain.linearRampToValueAtTime(音量, this.容器.currentTime)
        oscillator.start(this.容器.currentTime)
        gainNode.gain.exponentialRampToValueAtTime(0.001, this.容器.currentTime + 1)
        oscillator.stop(this.容器.currentTime + 1)

    彈鍵: (鍵, 音量) ->
        this.播音(this.取頻率(鍵), 音量)

    連彈: (譜, 音量 = 0.3, 間隔 = 100) ->
        s = 0
        go = (that) ->
            鍵 = 譜[s]
            s += 1
            if 鍵!=''
                that.彈鍵(鍵, 音量)
            if s < 譜.length
                setTimeout(->
                    go(that)
                , 間隔)
        go(this)

# window.onload = ->
#     eleButton = document.getElementById('a')

#     eleButton.addEventListener('mouseenter', ->
#         # 琴.連彈(audioCtx, 碎月)
#         琴.連彈([7, 6, 5, 4, 3, 2, 1], 0.2, 25)
#     )