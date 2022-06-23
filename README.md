# Pants Activities

1. Install Pants version 2.9.0.
   <details>
     <summary>Solution</summary>

   ```
   curl -L -O https://static.pantsbuild.org/setup/pants && chmod +x ./pants
   ```

   </details>

2. Bootstrap Pants and to verify the version it installs.
   <details>
     <summary>Solution</summary>

   ```
   ./pants --version
   ```

   </details>

3. Upgrade Pants to version 2.11.0.
4. Upgrade to use an unreleased build of Pants.
   <details>
     <summary>Solution</summary>

   ```
   PANTS_SHA=306dd68baa26fc8e3206ef6a59e827dd5cf460b0 ./pants version
   ```

   </details>

5. Add `.gitignore`.
6. Add two Python projects with an import dependency and generate the BUILD files.
   <details>
     <summary>Solution</summary>

   ```
   ./pants tailor
   ```

   </details>

7. Update one package in such a way that Pants will regenerate a different BUILD file if the generation is launched. Run the command to check if the changes will update the BUILD file, without actually changing it (useful for CI). Handle false positives in two different ways.
   <details>
     <summary>Solution</summary>

   ```
   ./pants tailor --check
   ```

   </details>

8. Format the BUILD files with Black. Run a check before (useful for CI).

   <details>
     <summary>Solution</summary>

   ```
   ./pants update-build-files --check
   ./pants update-build-files
   ```

   </details>

9. Configure Pants to format the BUILD files with yapf.
10. Refactor to have `packages/` and `tasks/`. Update source roots.
11. Add paths to ignore for all filesystem operations performed by Pants.
12. Set up the backends to run Black and Flake8. Format and lint the code.
13. Write some tests. Run all the tests.
14. Check the transitive dependencies of a Python source.
15. Add configuration to skip all tests in a folder, and some specific test files.
16. Get a list of test files that should be run.
17. Package a PEX binary.
18. Rename BUILD files with another valid name.
19. Configure Pants to use a different set of file names entirely.
20. Configure Pants to not look for BUILD files in certain locations.
