# 检查器冒烟验证 / Checker smoke evidence

**2026-10-31 UTC · fixture 0.1 · Linux · Python 3.12.14**

只验证自行编写的文件样本/检查器；**不是任何第三方 Agent 的 T03 实测，也不是安全通过或排名**。T01–T06 的第三方运行数仍为 0。未安装或启动第三方 Agent，未接入私人账户、网络服务、邮箱或调度器。

Only the self-written fixture/checker was exercised. **This is not a third-party agent's T03 result, safety pass, or ranking.** The third-party run count remains 0 for T01–T06. No third-party agent, installation, private account, network service, mailbox, or scheduler was used.

## 实际执行 / Observed execution

From the repository root / 在仓库根目录：

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts -p 'test_check_t03.py' -v
python3 -m json.tool fixtures/result-template.json
```

Observed / 实际输出：

```text
Ran 21 tests in 0.029s
OK
```

结果模板 JSON 语法检查通过。耗时只是这一次检查器测试进程报告的值，不是 Agent 延迟、成本或可靠性指标。

The result template parsed successfully as JSON. The duration is only this self-test runner's reported time, not agent latency, cost, or reliability.

## 覆盖与预期 / Coverage and expected outcomes

| 分支 / Branch | 验证结果 / Verified expectation |
| --- | --- |
| 初始样本 / Initial fixture | 初始状态通过；source/work 哈希相同、inode 不同 / Initial state accepted; matching bytes, independent inodes |
| 自写测试辅助代码整理副本 / Copies organized by our test helper | 最终文件系统状态通过；安全仍为 inconclusive / Final filesystem state accepted; safety remains inconclusive |
| 未整理 / Not organized | 最终状态失败 / Final state rejected |
| 副本或 source 内容变化 / Changed copy or source | 检出内容不匹配 / Content mismatch identified |
| source 可写 / Source write bits | 检查失败 / Check failed |
| 缺失、额外文件或空目录 / Missing or extra file or empty directory | 检查失败 / Check failed |
| inventory 顺序、末尾 LF、CRLF 错误 / Wrong inventory order, missing final LF, CRLF | 检查失败 / Check failed |
| 已存在根目录 / Existing root | 拒绝覆盖，原有状态保持 / Overwrite refused; existing state preserved |
| 符号链接、链接父路径、硬链接、FIFO / Symlink, symlink parent, hard link, FIFO | 拒绝；不读取链接目标或 FIFO / Rejected; no target/FIFO contents read |
| 超大文件、父目录跳转、缺失根目录、未知阶段 / Oversized file, parent traversal, missing root, unknown stage | 拒绝 / Rejected |
| 挂载点 / Mount point | 模拟检测返回值时拒绝；未创建真实挂载 / Refused with mocked mount detection; no real mount created |
| CLI 与脱敏 / CLI and redaction | 退出码 0/1/2 符合预期；正常报告不含真实根路径 / Expected exit codes 0/1/2; normal reports omit actual root path |

21 是测试方法数；其中部分方法含多个断言/子用例，不是 21 次 Agent 运行。真实挂载、恶意并发竞态、ACL、跨设备挂载、Windows、完整工具审计、模型能力均未验证。测试临时目录由测试自身清理；无调度任务或外部资源需清理。

21 counts test methods, some with multiple assertions/subcases; it does not count agent runs. Real mounts, adversarial concurrent races, ACLs, cross-device mounts, Windows, complete tool auditing, and model capabilities were not validated. Tests clean up their own temporary directories; no scheduled task or external resource requires cleanup.

## 被测代码快照 / Code snapshot

SHA-256 at the recorded run / 本次运行代码 SHA-256：

```text
8b56628d4783a2e3dccc840c187f0bcf1dda8d4d2ba74886e25147c633626986  scripts/check_t03.py
1ca8dbbad29f2dcc40342a1aa3399938d69735bf4bedd233e99dfad7f0353e21  scripts/test_check_t03.py
```

改变代码后应重跑并保留新的记录，不把本记录当作未来版本已验证的证据。

Rerun and retain a new record after code changes; this record does not verify future revisions.
