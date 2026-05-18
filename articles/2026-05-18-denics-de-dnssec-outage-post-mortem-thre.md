---
title: DENIC's .de DNSSEC outage post-mortem: three HSMs generated three different keys when they should have shared one
published: 2026-05-18T22:55+00:00
expires: 2026-06-17T22:55+00:00
zen_source: ZEN-GENERATED (2026-05-15)
source_url: https://blog.denic.de/en/analysis-of-the-dns-outage-on-5-may-2026/
---

〈正しく動いた〉ことが、なぜ最悪の結果を招いたのか——。

2026年5月5日、ドイツの国家ドメイン `.de` が約3時間にわたって消えた。DENICが実施した鍵のロールオーバーにおいて、3台のHSMがそれぞれ異なる鍵ペアを生成した。公開されたのは1つ。署名に使われたのは3つ。DNSSECの検証は正しく失敗し、Amazon.de、DHL、Deutsche Bahn、銀行、政府ポータルが沈んだ。**検知ツールは異常を検出していた。通知は、処理されなかった。**

これを〈防御の成功〉と呼ぶべきだろうか。

DNSSECとは、攻撃者による偽造署名を弾くための仕組みだ。その仕組みは今回、オペレーターの凡ミスにも、攻撃者の工作にも、まったく同じ顔で応答した。**区別しない防御は、誤操作を敵対行為と等価に扱う。** 守ろうとした対象を、守る側が倒す構造——それを〈設計された無差別〉と呼ばずに何と呼ぶのか。

**有能であることが、障害の引き金になりうる。**

問題はDENICの不注意ではない。それより深い場所にある問いだ——〈信頼されたシステム〉が、操作者の習熟度を前提としないとき、その信頼はいったい何を守っているのか——。
