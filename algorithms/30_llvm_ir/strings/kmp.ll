; ModuleID = 'algorithms/02_c/strings/kmp.c'
source_filename = "algorithms/02_c/strings/kmp.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [13 x i8] c"Found at %d\0A\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @compute_lps(ptr noundef readonly captures(none) %0, i32 noundef %1, ptr noundef captures(none) initializes((0, 4)) %2) local_unnamed_addr #0 {
  store i32 0, ptr %2, align 4, !tbaa !5
  %4 = icmp sgt i32 %1, 1
  br i1 %4, label %6, label %5

5:                                                ; preds = %29, %3
  ret void

6:                                                ; preds = %3, %29
  %7 = phi i32 [ %31, %29 ], [ 1, %3 ]
  %8 = phi i32 [ %30, %29 ], [ 0, %3 ]
  %9 = sext i32 %7 to i64
  %10 = getelementptr inbounds i8, ptr %0, i64 %9
  %11 = load i8, ptr %10, align 1, !tbaa !9
  %12 = sext i32 %8 to i64
  %13 = getelementptr inbounds i8, ptr %0, i64 %12
  %14 = load i8, ptr %13, align 1, !tbaa !9
  %15 = icmp eq i8 %11, %14
  br i1 %15, label %16, label %20

16:                                               ; preds = %6
  %17 = add nsw i32 %8, 1
  %18 = add nsw i32 %7, 1
  %19 = getelementptr inbounds i32, ptr %2, i64 %9
  store i32 %17, ptr %19, align 4, !tbaa !5
  br label %29

20:                                               ; preds = %6
  %21 = icmp eq i32 %8, 0
  br i1 %21, label %26, label %22

22:                                               ; preds = %20
  %23 = getelementptr i32, ptr %2, i64 %12
  %24 = getelementptr i8, ptr %23, i64 -4
  %25 = load i32, ptr %24, align 4, !tbaa !5
  br label %29

26:                                               ; preds = %20
  %27 = add nsw i32 %7, 1
  %28 = getelementptr inbounds i32, ptr %2, i64 %9
  store i32 0, ptr %28, align 4, !tbaa !5
  br label %29

29:                                               ; preds = %22, %26, %16
  %30 = phi i32 [ %17, %16 ], [ %25, %22 ], [ 0, %26 ]
  %31 = phi i32 [ %18, %16 ], [ %7, %22 ], [ %27, %26 ]
  %32 = icmp slt i32 %31, %1
  br i1 %32, label %6, label %5, !llvm.loop !10
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local void @kmp(ptr noundef readonly captures(none) %0, ptr noundef readonly captures(none) %1) local_unnamed_addr #1 {
  %3 = tail call i64 @strlen(ptr noundef nonnull dereferenceable(1) %0) #4
  %4 = trunc i64 %3 to i32
  %5 = tail call i64 @strlen(ptr noundef nonnull dereferenceable(1) %1) #4
  %6 = trunc i64 %5 to i32
  %7 = and i64 %5, 4294967295
  %8 = alloca i32, i64 %7, align 16
  store i32 0, ptr %8, align 16, !tbaa !5
  %9 = icmp sgt i32 %6, 1
  br i1 %9, label %10, label %37

10:                                               ; preds = %2, %33
  %11 = phi i32 [ %35, %33 ], [ 1, %2 ]
  %12 = phi i32 [ %34, %33 ], [ 0, %2 ]
  %13 = sext i32 %11 to i64
  %14 = getelementptr inbounds i8, ptr %1, i64 %13
  %15 = load i8, ptr %14, align 1, !tbaa !9
  %16 = sext i32 %12 to i64
  %17 = getelementptr inbounds i8, ptr %1, i64 %16
  %18 = load i8, ptr %17, align 1, !tbaa !9
  %19 = icmp eq i8 %15, %18
  br i1 %19, label %20, label %24

20:                                               ; preds = %10
  %21 = add nsw i32 %12, 1
  %22 = add nsw i32 %11, 1
  %23 = getelementptr inbounds i32, ptr %8, i64 %13
  store i32 %21, ptr %23, align 4, !tbaa !5
  br label %33

24:                                               ; preds = %10
  %25 = icmp eq i32 %12, 0
  br i1 %25, label %30, label %26

26:                                               ; preds = %24
  %27 = getelementptr i32, ptr %8, i64 %16
  %28 = getelementptr i8, ptr %27, i64 -4
  %29 = load i32, ptr %28, align 4, !tbaa !5
  br label %33

30:                                               ; preds = %24
  %31 = add nsw i32 %11, 1
  %32 = getelementptr inbounds i32, ptr %8, i64 %13
  store i32 0, ptr %32, align 4, !tbaa !5
  br label %33

33:                                               ; preds = %30, %26, %20
  %34 = phi i32 [ %21, %20 ], [ %29, %26 ], [ 0, %30 ]
  %35 = phi i32 [ %22, %20 ], [ %11, %26 ], [ %31, %30 ]
  %36 = icmp slt i32 %35, %6
  br i1 %36, label %10, label %37, !llvm.loop !10

37:                                               ; preds = %33, %2
  %38 = icmp sgt i32 %4, 0
  br i1 %38, label %39, label %87

39:                                               ; preds = %37
  %40 = shl i64 %5, 32
  %41 = ashr exact i64 %40, 30
  %42 = getelementptr i8, ptr %8, i64 %41
  %43 = getelementptr i8, ptr %42, i64 -4
  br label %44

44:                                               ; preds = %39, %83
  %45 = phi i32 [ %85, %83 ], [ 0, %39 ]
  %46 = phi i32 [ %84, %83 ], [ 0, %39 ]
  %47 = sext i32 %46 to i64
  %48 = getelementptr inbounds i8, ptr %0, i64 %47
  %49 = load i8, ptr %48, align 1, !tbaa !9
  %50 = sext i32 %45 to i64
  %51 = getelementptr inbounds i8, ptr %1, i64 %50
  %52 = load i8, ptr %51, align 1, !tbaa !9
  %53 = icmp eq i8 %49, %52
  %54 = zext i1 %53 to i32
  %55 = add nsw i32 %46, %54
  %56 = add nsw i32 %45, %54
  %57 = icmp eq i32 %56, %6
  br i1 %57, label %58, label %62

58:                                               ; preds = %44
  %59 = sub nsw i32 %55, %6
  %60 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %59)
  %61 = load i32, ptr %43, align 4, !tbaa !5
  br label %83

62:                                               ; preds = %44
  %63 = icmp slt i32 %55, %4
  br i1 %63, label %64, label %83

64:                                               ; preds = %62
  %65 = sext i32 %55 to i64
  %66 = getelementptr inbounds i8, ptr %0, i64 %65
  %67 = load i8, ptr %66, align 1, !tbaa !9
  %68 = sext i32 %56 to i64
  %69 = getelementptr inbounds i8, ptr %1, i64 %68
  %70 = load i8, ptr %69, align 1, !tbaa !9
  %71 = icmp eq i8 %67, %70
  br i1 %71, label %83, label %72

72:                                               ; preds = %64
  %73 = icmp eq i32 %56, 0
  br i1 %73, label %78, label %74

74:                                               ; preds = %72
  %75 = getelementptr i32, ptr %8, i64 %68
  %76 = getelementptr i8, ptr %75, i64 -4
  %77 = load i32, ptr %76, align 4, !tbaa !5
  br label %78

78:                                               ; preds = %72, %74
  %79 = phi i32 [ %77, %74 ], [ 0, %72 ]
  %80 = icmp eq i32 %79, 0
  %81 = zext i1 %80 to i32
  %82 = add nsw i32 %55, %81
  br label %83

83:                                               ; preds = %62, %64, %78, %58
  %84 = phi i32 [ %55, %58 ], [ %82, %78 ], [ %55, %64 ], [ %55, %62 ]
  %85 = phi i32 [ %61, %58 ], [ %79, %78 ], [ %56, %64 ], [ %56, %62 ]
  %86 = icmp slt i32 %84, %4
  br i1 %86, label %44, label %87, !llvm.loop !12

87:                                               ; preds = %83, %37
  ret void
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: read)
declare i64 @strlen(ptr noundef captures(none)) local_unnamed_addr #2

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #3

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: read) "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { nounwind willreturn memory(read) }

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
!9 = !{!7, !7, i64 0}
!10 = distinct !{!10, !11}
!11 = !{!"llvm.loop.mustprogress"}
!12 = distinct !{!12, !11}
