const inputKeyword = document.getElementById("fileName");
const buttonSearch = document.getElementById('search');
const targetElement = document.getElementById("tableTarget");

buttonSearch.addEventListener('click', () => {
    let urlKeyword = encodeURIComponent(inputKeyword.value.trim())
    fetch(`${window.location.href}api?f=${urlKeyword}`)
        .then(response => response.json())
        .then(data => {
            if (data.status == "error") {
                targetElement.innerHTML = "未搜索到此文件！"
                return;
            }
            let table = document.createElement("table");
            let index = 1;
            data.data.forEach(element => {
                let row = table.insertRow();
                let [cell1, cell2, cell3] = [row.insertCell(0), row.insertCell(1), row.insertCell(2)]
                if (element.repo !== "archlinuxcn") {
                    let pkg_url = `https://archlinux.org/packages/${element.repo}/x86_64/${element.name}`
                    cell1.innerHTML = `<div class="cell">${element.repo}/${element.name}<sup> <a href="${pkg_url}">pkg</a></sup></div>`;
                } else {
                    cell1.innerHTML = `<div class="cell">${element.repo}/${element.name}</div>`;
                }
                cell2.innerHTML = `<div class="cell">${element.ver}</div>`;
                cell3.innerHTML = `<div class="cell">${element.path}</div>`;
                cell1.style.verticalAlign = "top"
                cell2.style.verticalAlign = "top"
                index++;
            });
            targetElement.innerHTML = table.outerHTML;
        });
});
inputKeyword.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        buttonSearch.click();
    }
});