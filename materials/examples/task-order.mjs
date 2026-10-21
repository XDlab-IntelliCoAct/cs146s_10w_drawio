// 搜索结果顺序示例，可直接用 Node 运行。
let visibleWithoutGuard = ""
let visibleWithGuard = ""
let latestRequest = 0

function search(query) {
    const id = ++latestRequest
    return {
        complete(value) {
            visibleWithoutGuard = value
            if (id === latestRequest) {
                visibleWithGuard = value
            }
            console.log(JSON.stringify({ query, id, latestRequest, visibleWithoutGuard, visibleWithGuard }))
        },
    }
}

const first = search("旧查询")
const second = search("新查询")
second.complete("新结果")
first.complete("旧结果")
if (visibleWithoutGuard !== "旧结果" || visibleWithGuard !== "新结果") {
    throw new Error("示例结果与预期不符")
}
