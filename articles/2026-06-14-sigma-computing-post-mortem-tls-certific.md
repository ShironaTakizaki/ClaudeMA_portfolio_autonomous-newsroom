---
title: Sigma Computing Post-Mortem: TLS Certificate Rotation Connectivity Disruption Caused by Third-Party Certificate Bundling
published: 2026-06-14T23:03+00:00
expires: 2026-07-14T23:03+00:00
zen_source: ZEN-GENERATED (2026-05-14)
source_url: https://community.sigmacomputing.com/t/post-mortem-for-tls-certificate-rotation-connectivity-disruption/6963
---

「変更は完了した」と、誰が決めるのか。

2026年5月末から6月初旬にかけて、Sigma Computingの一部顧客が認証エラーに見舞われた。原因は〈ルーティンな作業〉——TLS証明書のローテーションだった。しかし問題は自社ではなく、証明書バンドルを組み立てた上流ベンダーの側にあった。修正が展開されるまで、数日間かかった。

**変えたのは証明書だ。変えていなかったのは、その証明書を信頼していたすべての前提だった。**

これを〈不完全な変更〉と呼ぶのは簡単だ。だが問いはもっと深い場所にある。「自分が変えた対象に同意していた他の誰かを、私は把握していたか」——。

〈委託〉という行為が持つ本質的な欺瞞がある。誰かに渡した瞬間、私たちは理解したふりをやめる。検証を委ねることを、信頼と呼ぶ。上流を信じることを、効率と呼ぶ。そしてその〈信頼〉が崩れたとき、私たちは「ベンダーの問題だった」と言う。

**正確には、ベンダーの問題ではない。確認しなかった、私たちの問題だ。**

これはTLS証明書の話ではない。あなたが昨日変更を加えたシステム——設計、言葉、ルール、関係——の中で、まだ古い前提のまま動いているものが、いくつあるだろうか。
