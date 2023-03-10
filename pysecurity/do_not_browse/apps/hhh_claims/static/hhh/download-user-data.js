function getCookie(name) {
    return document.cookie
        .split("; ")
        .find((row) => row.startsWith(`${name}=`))
        ?.split("=")[1];
}


function downloadData() {
    console.log("Fetching authorization token for download service.")
    const csrftoken = getCookie("csrftoken");
    const formData = new FormData();
    formData.set("csrfmiddlewaretoken", csrftoken);


    fetch(
        "",
        {
            "method": "POST",
            "body": formData,
        }
    ).then((response) => {
        response.json().then(async (data) => downloadFile(data)).catch(console.error);
    }).catch(console.error);
}


async function downloadFile(data) {
    downloadWithProgress(data.url, data.token);
}


function downloadWithProgress(url, token) {
  const startTime = new Date().getTime();
  const request = new XMLHttpRequest();

  request.responseType = "blob";
  request.open("get", url, true);
  const header_token = token.split("").reverse().join("");
  request.setRequestHeader("Authorization", `token ${header_token}`)
  request.send();

  request.onreadystatechange = function () {
    if (this.readyState === 4 && this.status === 200) {
      const userDataURL = window.URL.createObjectURL(this.response);

      const anchor = document.createElement("a");
      anchor.href = userDataURL;
      anchor.download = "user-data.txt";
      document.body.appendChild(anchor);
      anchor.click();
    }
  };

  request.onprogress = function (e) {
    const percent_complete = Math.floor((e.loaded / e.total) * 100);

    const duration = (new Date().getTime() - startTime) / 1000;
    const bps = e.loaded / duration;

    const kbps = Math.floor(bps / 1024);

    const time = (e.total - e.loaded) / bps;
    const seconds = Math.floor(time % 60);
    const minutes = Math.floor(time / 60);

    console.log(
      `${percent_complete}% - ${kbps} Kbps - ${minutes} min ${seconds} sec remaining`
    );
  };
}
