class Main {
    

    run() : void {
        const url = window.location.href;
        const re = new RegExp('\/shorts\/');
        if (re.test(url)) {
            const url_treated = url.split("/")[4];
            const url_base = 'https://www.youtube.com/watch';
            const new_url = `${url_base}?v=${url_treated}`;
            window.location.href = new_url;
        }
    }

}

const main = new Main();

const interval = setInterval(() => {
    main.run();
}, 1000);