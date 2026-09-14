; ModuleID = 'algorithms/02_c/sorting/quick_sort.c'
source_filename = "algorithms/02_c/sorting/quick_sort.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: mustprogress nofree norecurse nosync nounwind sspstrong willreturn memory(argmem: readwrite) uwtable
define dso_local void @swap(ptr noundef captures(none) %0, ptr noundef captures(none) %1) local_unnamed_addr #0 {
  %3 = load i32, ptr %0, align 4, !tbaa !5
  %4 = load i32, ptr %1, align 4, !tbaa !5
  store i32 %4, ptr %0, align 4, !tbaa !5
  store i32 %3, ptr %1, align 4, !tbaa !5
  ret void
}

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local range(i32 -2147483647, -2147483648) i32 @partition(ptr noundef captures(none) %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #1 {
  %4 = sext i32 %2 to i64
  %5 = getelementptr inbounds i32, ptr %0, i64 %4
  %6 = load i32, ptr %5, align 4, !tbaa !5
  %7 = icmp slt i32 %1, %2
  br i1 %7, label %8, label %35

8:                                                ; preds = %3
  %9 = add nsw i32 %1, -1
  %10 = sext i32 %1 to i64
  %11 = sub nsw i64 %4, %10
  %12 = and i64 %11, 1
  %13 = icmp eq i64 %12, 0
  br i1 %13, label %25, label %14

14:                                               ; preds = %8
  %15 = getelementptr inbounds i32, ptr %0, i64 %10
  %16 = load i32, ptr %15, align 4, !tbaa !5
  %17 = icmp sgt i32 %16, %6
  br i1 %17, label %22, label %18

18:                                               ; preds = %14
  %19 = sext i32 %1 to i64
  %20 = getelementptr inbounds i32, ptr %0, i64 %19
  %21 = load i32, ptr %20, align 4, !tbaa !5
  store i32 %16, ptr %20, align 4, !tbaa !5
  store i32 %21, ptr %15, align 4, !tbaa !5
  br label %22

22:                                               ; preds = %18, %14
  %23 = phi i32 [ %1, %18 ], [ %9, %14 ]
  %24 = add nsw i64 %10, 1
  br label %25

25:                                               ; preds = %22, %8
  %26 = phi i32 [ poison, %8 ], [ %23, %22 ]
  %27 = phi i64 [ %10, %8 ], [ %24, %22 ]
  %28 = phi i32 [ %9, %8 ], [ %23, %22 ]
  %29 = add nsw i64 %4, -1
  %30 = icmp eq i64 %29, %10
  br i1 %30, label %31, label %41

31:                                               ; preds = %63, %25
  %32 = phi i32 [ %26, %25 ], [ %64, %63 ]
  %33 = load i32, ptr %5, align 4, !tbaa !5
  %34 = add nsw i32 %32, 1
  br label %35

35:                                               ; preds = %31, %3
  %36 = phi i32 [ %6, %3 ], [ %33, %31 ]
  %37 = phi i32 [ %1, %3 ], [ %34, %31 ]
  %38 = sext i32 %37 to i64
  %39 = getelementptr inbounds i32, ptr %0, i64 %38
  %40 = load i32, ptr %39, align 4, !tbaa !5
  store i32 %36, ptr %39, align 4, !tbaa !5
  store i32 %40, ptr %5, align 4, !tbaa !5
  ret i32 %37

41:                                               ; preds = %25, %63
  %42 = phi i64 [ %65, %63 ], [ %27, %25 ]
  %43 = phi i32 [ %64, %63 ], [ %28, %25 ]
  %44 = getelementptr inbounds i32, ptr %0, i64 %42
  %45 = load i32, ptr %44, align 4, !tbaa !5
  %46 = icmp sgt i32 %45, %6
  br i1 %46, label %52, label %47

47:                                               ; preds = %41
  %48 = add nsw i32 %43, 1
  %49 = sext i32 %48 to i64
  %50 = getelementptr inbounds i32, ptr %0, i64 %49
  %51 = load i32, ptr %50, align 4, !tbaa !5
  store i32 %45, ptr %50, align 4, !tbaa !5
  store i32 %51, ptr %44, align 4, !tbaa !5
  br label %52

52:                                               ; preds = %41, %47
  %53 = phi i32 [ %48, %47 ], [ %43, %41 ]
  %54 = getelementptr i32, ptr %0, i64 %42
  %55 = getelementptr i8, ptr %54, i64 4
  %56 = load i32, ptr %55, align 4, !tbaa !5
  %57 = icmp sgt i32 %56, %6
  br i1 %57, label %63, label %58

58:                                               ; preds = %52
  %59 = add nsw i32 %53, 1
  %60 = sext i32 %59 to i64
  %61 = getelementptr inbounds i32, ptr %0, i64 %60
  %62 = load i32, ptr %61, align 4, !tbaa !5
  store i32 %56, ptr %61, align 4, !tbaa !5
  store i32 %62, ptr %55, align 4, !tbaa !5
  br label %63

63:                                               ; preds = %58, %52
  %64 = phi i32 [ %59, %58 ], [ %53, %52 ]
  %65 = add nsw i64 %42, 2
  %66 = icmp eq i64 %65, %4
  br i1 %66, label %31, label %41, !llvm.loop !9
}

; Function Attrs: nofree nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @quick_sort(ptr noundef captures(none) %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #2 {
  %4 = icmp slt i32 %1, %2
  br i1 %4, label %5, label %68

5:                                                ; preds = %3
  %6 = sext i32 %2 to i64
  %7 = getelementptr inbounds i32, ptr %0, i64 %6
  %8 = add nsw i64 %6, -1
  br label %9

9:                                                ; preds = %5, %59
  %10 = phi i32 [ %1, %5 ], [ %66, %59 ]
  %11 = load i32, ptr %7, align 4, !tbaa !5
  %12 = add nsw i32 %10, -1
  %13 = sext i32 %10 to i64
  %14 = sub nsw i64 %6, %13
  %15 = and i64 %14, 1
  %16 = icmp eq i64 %15, 0
  br i1 %16, label %28, label %17

17:                                               ; preds = %9
  %18 = getelementptr inbounds i32, ptr %0, i64 %13
  %19 = load i32, ptr %18, align 4, !tbaa !5
  %20 = icmp sgt i32 %19, %11
  br i1 %20, label %25, label %21

21:                                               ; preds = %17
  %22 = sext i32 %10 to i64
  %23 = getelementptr inbounds i32, ptr %0, i64 %22
  %24 = load i32, ptr %23, align 4, !tbaa !5
  store i32 %19, ptr %23, align 4, !tbaa !5
  store i32 %24, ptr %18, align 4, !tbaa !5
  br label %25

25:                                               ; preds = %21, %17
  %26 = phi i32 [ %10, %21 ], [ %12, %17 ]
  %27 = add nsw i64 %13, 1
  br label %28

28:                                               ; preds = %25, %9
  %29 = phi i32 [ poison, %9 ], [ %26, %25 ]
  %30 = phi i64 [ %13, %9 ], [ %27, %25 ]
  %31 = phi i32 [ %12, %9 ], [ %26, %25 ]
  %32 = icmp eq i64 %8, %13
  br i1 %32, label %59, label %33

33:                                               ; preds = %28, %55
  %34 = phi i64 [ %57, %55 ], [ %30, %28 ]
  %35 = phi i32 [ %56, %55 ], [ %31, %28 ]
  %36 = getelementptr inbounds i32, ptr %0, i64 %34
  %37 = load i32, ptr %36, align 4, !tbaa !5
  %38 = icmp sgt i32 %37, %11
  br i1 %38, label %44, label %39

39:                                               ; preds = %33
  %40 = add nsw i32 %35, 1
  %41 = sext i32 %40 to i64
  %42 = getelementptr inbounds i32, ptr %0, i64 %41
  %43 = load i32, ptr %42, align 4, !tbaa !5
  store i32 %37, ptr %42, align 4, !tbaa !5
  store i32 %43, ptr %36, align 4, !tbaa !5
  br label %44

44:                                               ; preds = %39, %33
  %45 = phi i32 [ %40, %39 ], [ %35, %33 ]
  %46 = getelementptr i32, ptr %0, i64 %34
  %47 = getelementptr i8, ptr %46, i64 4
  %48 = load i32, ptr %47, align 4, !tbaa !5
  %49 = icmp sgt i32 %48, %11
  br i1 %49, label %55, label %50

50:                                               ; preds = %44
  %51 = add nsw i32 %45, 1
  %52 = sext i32 %51 to i64
  %53 = getelementptr inbounds i32, ptr %0, i64 %52
  %54 = load i32, ptr %53, align 4, !tbaa !5
  store i32 %48, ptr %53, align 4, !tbaa !5
  store i32 %54, ptr %47, align 4, !tbaa !5
  br label %55

55:                                               ; preds = %50, %44
  %56 = phi i32 [ %51, %50 ], [ %45, %44 ]
  %57 = add nsw i64 %34, 2
  %58 = icmp eq i64 %57, %6
  br i1 %58, label %59, label %33, !llvm.loop !9

59:                                               ; preds = %55, %28
  %60 = phi i32 [ %29, %28 ], [ %56, %55 ]
  %61 = load i32, ptr %7, align 4, !tbaa !5
  %62 = sext i32 %60 to i64
  %63 = getelementptr i32, ptr %0, i64 %62
  %64 = getelementptr i8, ptr %63, i64 4
  %65 = load i32, ptr %64, align 4, !tbaa !5
  store i32 %61, ptr %64, align 4, !tbaa !5
  store i32 %65, ptr %7, align 4, !tbaa !5
  tail call void @quick_sort(ptr noundef nonnull %0, i32 noundef %10, i32 noundef %60)
  %66 = add nsw i32 %60, 2
  %67 = icmp slt i32 %66, %2
  br i1 %67, label %9, label %68

68:                                               ; preds = %59, %3
  ret void
}

attributes #0 = { mustprogress nofree norecurse nosync nounwind sspstrong willreturn memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nofree nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
