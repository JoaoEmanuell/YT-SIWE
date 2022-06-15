export interface RedirectInterface {
    readonly url : string;

    validate_url() : boolean;

    run_redirect() : void;
}