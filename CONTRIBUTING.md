# Contributing to Data Engineering Practice Problems

Thank you for wanting to contribute! This document provides guidelines and instructions for contributing to this repository.

## How to Contribute

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/Data-Engineering-UpWeGo.git
cd Data-Engineering-UpWeGo
```

### 2. Create a Branch

```bash
git checkout -b feature/exercise-X-solution
```

Use descriptive branch names:
- `feature/exercise-5-solution` - For a completed solution
- `docs/exercise-3-improvements` - For documentation improvements
- `fix/dockerfile-issue` - For bug fixes

### 3. Make Your Changes

#### Submitting Solutions

When you complete an exercise:

1. **Test your solution locally:**
   ```bash
   cd Exercises/Exercise-X
   docker-compose build
   docker-compose run app python solution.py
   ```

2. **Ensure your code:**
   - Follows Python PEP 8 style guide
   - Includes docstrings for all functions
   - Has inline comments explaining complex logic
   - Handles errors gracefully
   - Is well-tested

3. **Update the README if needed:**
   - Note any special setup requirements
   - Document any deviations from the original problem
   - Add performance metrics if applicable

#### Submitting Enhancements

When improving exercises:

1. Keep changes focused on a single exercise
2. Add bonus challenges if applicable
3. Update documentation
4. Ensure backwards compatibility

### 4. Commit Your Changes

```bash
git add .
git commit -m "Complete Exercise 5: Data Modeling for Postgres"
```

Use clear, descriptive commit messages:
- ✓ Good: "Complete Exercise 5 with schema design and data ingestion"
- ✗ Bad: "fix stuff"

### 5. Push to Your Fork

```bash
git push origin feature/exercise-X-solution
```

### 6. Create a Pull Request

1. Go to the original repository
2. Click "New Pull Request"
3. Select your branch
4. Fill in the PR template with:
   - Which exercise(s) you're working on
   - What you implemented
   - Any challenges or notes
   - Test results/evidence

## Solution Quality Standards

Your solution should demonstrate:

### Code Quality
- ✓ Proper error handling
- ✓ Clear variable and function names
- ✓ DRY (Don't Repeat Yourself) principles
- ✓ Appropriate use of libraries
- ✓ No hardcoded values
- ✓ Proper logging/output

### Documentation
- ✓ Docstrings for all functions
- ✓ Comments explaining complex logic
- ✓ README examples
- ✓ Performance notes if relevant

### Testing
- ✓ Works with provided sample data
- ✓ Handles edge cases
- ✓ Graceful error handling
- ✓ Tested locally with Docker

## Types of Contributions

### Solutions
Complete any exercise by filling in the TODO sections in `solution.py`.

### Documentation
- Improve existing READMEs
- Add tips and tricks
- Clarify confusing sections
- Add performance tips
- Provide troubleshooting guides

### Bug Fixes
- Fix issues in sample data
- Correct errors in READMEs
- Fix Dockerfile issues
- Resolve dependency problems

### New Content
- Additional bonus challenges
- Example implementations
- Performance optimizations
- Testing strategies

## Pull Request Process

1. **Fill out the PR template** - Include exercise number, what was done, and any notes

2. **Request review** - Tag maintainers for feedback

3. **Respond to feedback** - Address any comments or suggestions

4. **Get approval** - PRs require at least one approval before merging

5. **Celebrate!** - Your contribution is merged!

## Commit Guidelines

Follow these commit message conventions:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type:**
- `feat`: New feature or completed exercise
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests

**Scope:** Exercise number or area (e.g., `exercise-5`, `docs`, `docker`)

**Subject:** Use imperative mood, lowercase, no period

**Examples:**
```
feat(exercise-5): Add database schema with indexes
fix(exercise-3): Correct AWS credentials handling
docs(readme): Add bonus challenge information
refactor(exercise-7): Simplify PySpark aggregation
```

## Code Style

This project follows PEP 8 with these additions:

### Python Style
- Line length: max 100 characters
- Use type hints where possible
- Use f-strings for formatting
- Follow naming conventions:
  - `functions_with_underscores`
  - `CLASS_NAMES_IN_CAMELCASE`
  - `CONSTANTS_IN_ALL_CAPS`

### Shell Scripts
- Use consistent formatting
- Comment complex sections
- Test on both macOS and Linux if possible

## Testing

Before submitting:

1. **Build Docker image:**
   ```bash
   docker-compose build
   ```

2. **Run your solution:**
   ```bash
   docker-compose run app python solution.py
   ```

3. **Test with sample data:**
   - Verify it works as expected
   - Check edge cases
   - Ensure error handling works

## Communication

- Use GitHub Issues for questions/bugs
- Use Discussions for broader topics
- Be respectful and constructive
- Help others learn!

## Recognition

Contributors with accepted PRs will be:
- Added to CONTRIBUTORS.md
- Credited in commit history
- Highlighted in releases

## Licensing

By submitting a contribution, you agree that your code can be used under the MIT License.

## Questions?

- Open a GitHub Discussion
- Create an Issue
- Read existing solutions for examples

## Resources

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [How to Write Good Commit Messages](https://chris.beams.io/posts/git-commit/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

---

Thank you for contributing to improve data engineering education! 🚀
