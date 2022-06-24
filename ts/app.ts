import { Redirect } from './source/redirect';

class Main {
    run() : void {
        const url = window.location.href;
        const re = new RegExp('\/shorts\/');
        if (re.test(url)) {
            const redirect = new Redirect(url);
            redirect.run_redirect()
        }
    }

}

const main = new Main();

const interval = setInterval(() => {
    main.run();
}, 1000);