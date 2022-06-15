import { RedirectInterface } from "./interfaces/redirect_interface";

class Redirect implements RedirectInterface {
    readonly url : string;

    constructor(url : string) {
        this.url = url;
    }

    validate_url() : boolean {
        return true;
    }

    run_redirect() : void {
        window.location.href = this.url;
    }
}