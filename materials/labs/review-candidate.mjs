// 用于审查练习的虚构 PR 代码；根据练习约定编写测试并核验。
export function identity(issue) {
    return issue.cellId + ":" + issue.ruleId
}

export function unnamed(node) {
    return node.label.length === 0
}

export function summarize(result) {
    return {
        errors: result.issues?.filter(i => i.severity === "error").length ?? 0,
        warnings: result.issues?.filter(i => i.severity === "warning").length ?? 0,
    }
}

export function changed(before, after) {
    return JSON.stringify(before.issues) !== JSON.stringify(after.issues)
}
