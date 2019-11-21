from string import Template

n_files = 10
n_funcs = 10

func_template = Template("""
#[test]
fn test_${iter}() {
    let duration = time::Duration::from_millis(1000);
    let now = time::Instant::now();
    thread::sleep(duration);
    assert!(now.elapsed() >= duration);
}
""")

file_template = Template("""
use std::{thread, time};

${test_funcs}
""")

for file_i in range(n_files):
    funcs = []
    for func_i in range(n_funcs):
        funcs.append(func_template.substitute({'iter': str(func_i)}))
    output = file_template.substitute({'test_funcs': '\n'.join(funcs)})

    with open('tests/test_' + str(file_i) + '.rs', 'w') as f:
        f.write(output)
