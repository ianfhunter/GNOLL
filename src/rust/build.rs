use std::env;
use std::path::PathBuf;

fn main() {
    let manifest_dir = PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap());
    let gnoll_build = manifest_dir.join("../../build");
    println!(
        "cargo:rustc-link-search=native={}",
        gnoll_build.display()
    );
    println!("cargo:rustc-link-lib=dice");
}
