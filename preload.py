def preload(parser):   
    parser.add_argument(
        "--animatediff-model-path",
        type=str,
        help="Path to directory with AnimateDiff models",
        default=None,
    )