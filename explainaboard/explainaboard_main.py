import sys
import string
import argparse
import explainaboard.tasks

def main():
    parser = argparse.ArgumentParser(description='Interpretable Evaluation for NLP')


    parser.add_argument('--task', type=str, required=True,
                        help="absa")

    parser.add_argument('--ci', type=str, required=False, default= False,
                        help="True|False")

    parser.add_argument('--case', type=str, required=False, default= False,
                        help="True|False")

    parser.add_argument('--ece', type=str, required=False, default= False,
                        help="True|False")


    parser.add_argument('--type', type=str, required=False, default="single",
                        help="analysis type: single|pair|combine")
    parser.add_argument('--systems', type=str, required=True,
                        help="the directories of system outputs. Multiple one should be separated by comma, for example, system1,system2 (no space)")

    parser.add_argument('--output', type=str, required=True,
                        help="analysis output file")
    args = parser.parse_args()


    is_print_ci = args.ci
    is_print_case = args.case
    is_print_ece = args.ece

    task = args.task
    analysis_type = args.type
    systems = args.systems.split(",")
    output = args.output


    print("task", task)
    print("type", analysis_type)
    print("systems", systems)


    # fine grained analysis
    if task == "absa":
        explainaboard.tasks.absa.eval_spec.evaluate(task_type=task, analysis_type=analysis_type, systems=systems, output=output, is_print_ci = is_print_ci, is_print_case = is_print_case, is_print_ece = is_print_ece)
    elif task == "ner":
        explainaboard.tasks.ner.eval_spec.evaluate(task_type=task, analysis_type=analysis_type, systems=systems, output=output, is_print_ci = is_print_ci, is_print_case = is_print_case, is_print_ece = is_print_ece)
    elif task == "pos":
        explainaboard.tasks.pos.eval_spec.evaluate(task_type=task, analysis_type=analysis_type, systems=systems, output=output, is_print_ci = is_print_ci, is_print_case = is_print_case, is_print_ece = is_print_ece)
    elif task == "chunk":
        explainaboard.tasks.chunk.eval_spec.evaluate(task_type=task, analysis_type=analysis_type, systems=systems, output=output, is_print_ci = is_print_ci, is_print_case = is_print_case, is_print_ece = is_print_ece)
    elif task == "cws":
        explainaboard.tasks.cws.eval_spec.evaluate(task_type=task, analysis_type=analysis_type, systems=systems, output=output, is_print_ci = is_print_ci, is_print_case = is_print_case, is_print_ece = is_print_ece)
    elif task == "tc":
        explainaboard.tasks.tc.eval_spec.evaluate(task_type=task, analysis_type=analysis_type, systems=systems, output=output, is_print_ci = is_print_ci, is_print_case = is_print_case, is_print_ece = is_print_ece)
    elif task == "nli":
        explainaboard.tasks.nli.eval_spec.evaluate(task_type=task, analysis_type=analysis_type, systems=systems, output=output, is_print_ci = is_print_ci, is_print_case = is_print_case, is_print_ece = is_print_ece)
    elif task == "re":
        explainaboard.tasks.re.eval_spec.evaluate(task_type=task, analysis_type=analysis_type, systems=systems, output=output, is_print_ci = is_print_ci, is_print_case = is_print_case, is_print_ece = is_print_ece)




if __name__ == '__main__':
    main()
    # python explainaboard_main.py --task absa  --systems ./test-laptop.tsv --output ./output/a.json
    # python explainaboard_main.py --task ner --systems ./test-conll03.tsv --output ./a.json
    # python explainaboard_main.py --task re --systems ./test_re.tsv --output ./a.json
    # python eval_spec.py  --task re --case True --systems ./test_re.tsv --output a.json --ci True