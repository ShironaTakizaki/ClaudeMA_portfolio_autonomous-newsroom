---
title: Azure East US Power Failure Cascades into Multi-Day Copilot Outage; Backup Power Control Systems Failed in Sync
published: 2026-06-04T23:05+00:00
expires: 2026-07-04T23:05+00:00
zen_source: ZEN-GENERATED (2026-05-14)
source_url: https://windowsnews.ai/article/microsoft-copilot-down-azure-power-incident-causes-widespread-disruption-june-1-2026.421260
---

〈完了〉とは、いつ訪れるのだろう。

5月29日、雷雨がAzure東部データセンターの主電源を落とした。バックアップ電源制御システムは、まるで申し合わせたかのように、同期して沈黙した。電力は3日後に戻った。**だが、Copilotは戻らなかった。**

停電という〈解決済みの問題〉は、確かに解決されていた。問題は別の場所にあった——大規模モデルのチェックポイントを復元し、整合性を検証する時間を、誰も設計に折り込んでいなかった。

**古い仮定が、静かに残り続けていた。**

クラシックなクラウドワークロードなら、電源回復は即ち復旧を意味した。その〈合意〉は長年正しかった。だから誰も疑わなかった。大規模モデル推論という新しい存在がシステムに加わったとき、タイムアウト設計も、監視ロジックも、復旧手順書も——みな旧世界の速度を信じたまま眠っていた。

変化したのはモデルだけだった。**変化を知らなかったのは、モデル以外のすべてだった。**

これは稀な障害だろうか。それとも、私たちは毎日、何かを変えながら、その変化と〈合意していた他の全員〉に通知し忘れているだろうか——。
