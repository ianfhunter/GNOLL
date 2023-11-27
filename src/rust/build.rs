fn main() {
       // Link with your external library
       println!("cargo:rustc-link-lib=dice");
       // You might need to specify the library path if it's not in standard locations
       // println!("cargo:rustc-link-search=native=/path/to/library");
}
