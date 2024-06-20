
    {
        int cand = (hi + lo) / 2;
        if (cand == 0)
        {
            return length;
        }
        if (sorted[cand - 1] < idx && idx <= sorted[cand])
        {
            import_position = cand;
            break;
        }
        else if (idx <= sorted[cand - 1])