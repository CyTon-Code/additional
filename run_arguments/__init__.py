def run_arguments(args):
    """
    ./ant command *arguments - этот блок отвечает за исполнения аргументов при старте.
    """
    arguments = True
    # args = parser_args(args)
    from additional.run import run
    run(args)
    if arguments:
        # import sys
        # ant_arguments(sys.argv)
        pass
