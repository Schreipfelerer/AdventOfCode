use std::{fs, path::Path};

/// Read a specific file from a day folder using an absolute path relative to the project root
pub fn read_input_file(day: &str, file: &str) -> String {
    // 1. Get the path to the project root (where Cargo.toml is)
    let manifest_dir = env!("CARGO_MANIFEST_DIR");

    // 2. Construct the absolute path
    let path = Path::new(manifest_dir)
        .join("src")
        .join(day)
        .join(file);
    
    // Convert the PathBuf into a displayable string for the error message
    let path_display = path.display().to_string();

    // 3. Read the file
    fs::read_to_string(&path)
        .unwrap_or_else(|err| {
            // Provide a better error message including the path that failed
            panic!("Failed to read input file at path: {} (Error: {})", path_display, err)
        })
}
