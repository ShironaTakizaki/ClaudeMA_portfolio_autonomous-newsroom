---
title: AWS US-EAST-1 thermal event: Coinbase's single-zone exchange went dark for 7 hours when backup systems failed
published: 2026-05-16T22:40+00:00
expires: 2026-06-15T22:40+00:00
zen_source: ZEN-GENERATED (2026-05-15)
source_url: https://www.singlestore.com/blog/aws-outage-may-2026-cross-region-disaster-recovery/
---

〈設計〉は、何と戦っていたのか——。

**2026年5月、AWS US-EAST-1の一室で冷却装置が止まった。** 熱が物理ストレージを侵し、Coinbaseの取引所は7時間、沈黙した。バックアップシステムは正しく動かなかった。エンジニアたちは夜通し、手動で復旧を試みた。

その沈黙の理由が、皮肉だ。

**Coinbaseは意図的に単一ゾーンへ処理を集中させていた。** 〈レイテンシ最小化〉という名の設計判断——それは卓越した合理性であり、同時に完璧な自傷だった。多重冗長化の守りは、「意図した集中」と「予期せぬ障害」を区別できない。**味方の作戦を、敵の侵攻と見分けられない防衛機構は、守備側の判断力そのものを破壊する。**

問い直してほしい。あなたの組織が誇る〈フェイルセーフ〉は、誰かの正しい判断を障害と誤認したとき、どう振る舞うか——。

**守ることに最適化されたシステムが、設計者の意図を踏み潰す。** これを失敗と呼ぶのか、それとも成功と呼ぶべきなのか。

その問いに今も、答えは出ていない。
